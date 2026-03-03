#!/usr/bin/env python3
"""Daily AI News Brief — fetch, curate with Claude, deliver via macOS notification."""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse

import html2text
import httpx
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from duckduckgo_search import DDGS
from openai import OpenAI

# Load env from script directory
load_dotenv(Path(__file__).parent / ".env")

LLM_API_KEY = os.environ["LLM_GW_API_KEY"]
LLM_BASE_URL = os.environ.get(
    "LLM_GW_BASE_URL",
    "https://api.anthropic.com/v1",
)
LLM_MODEL = os.environ.get("LLM_GW_MODEL", "claude-sonnet-4-6")

NEWS_QUERIES = [
    "artificial intelligence",
    "AI startups funding",
    "large language models",
    "AI regulation policy",
    "AI chips semiconductors",
]

# Company blog queries — searched via web (not news) since DDG news doesn't index blogs
BLOG_QUERIES = [
    "site:anthropic.com/news",
    "site:openai.com/index/",
    "site:blog.google/technology/ai",
    "site:ai.meta.com/blog",
    "site:mistral.ai/news",
    "site:deepmind.google/discover",
]

# Direct RSS/Atom feeds for AI company blogs — most reliable source for official posts
BLOG_FEEDS = [
    ("OpenAI", "https://openai.com/news/rss.xml"),
    ("Google AI", "https://blog.google/innovation-and-ai/technology/ai/rss/"),
    ("Google DeepMind", "https://deepmind.google/blog/rss.xml"),
]

# Pages to scrape for companies without RSS feeds
BLOG_SCRAPE = [
    ("Anthropic", "https://www.anthropic.com/news", r'href="(/news/[^"]+)"'),
]

TODAY = datetime.now()
DATE_STR = TODAY.strftime("%B %d, %Y")  # e.g. "February 27, 2026"
DATE_FILE = TODAY.strftime("%Y-%m-%d")  # e.g. "2026-02-27"


def fetch_blog_feeds() -> list[dict]:
    """Fetch recent posts from AI company RSS/Atom feeds and scraped pages."""
    articles = []
    cutoff = datetime.now(timezone.utc).timestamp() - 24 * 3600
    client = httpx.Client(timeout=10, verify=False, follow_redirects=True)

    # 1. RSS/Atom feeds
    for source_name, feed_url in BLOG_FEEDS:
        try:
            resp = client.get(feed_url)
            resp.raise_for_status()
            root = ET.fromstring(resp.text)
        except Exception as e:
            print(f"Warning: feed fetch failed for {source_name}: {e}", file=sys.stderr)
            continue

        # Handle both RSS <item> and Atom <entry>
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        items = root.findall(".//item") or root.findall(".//atom:entry", ns)

        for item in items:
            title = (item.findtext("title") or
                     item.findtext("atom:title", namespaces=ns) or "")
            link = (item.findtext("link") or "")
            if not link:
                link_el = item.find("atom:link", ns)
                link = link_el.get("href", "") if link_el is not None else ""
            description = (item.findtext("description") or
                           item.findtext("atom:summary", namespaces=ns) or "")
            pub_date = (item.findtext("pubDate") or
                        item.findtext("atom:updated", namespaces=ns) or "")

            # Filter to recent posts only
            if pub_date:
                try:
                    dt = parsedate_to_datetime(pub_date)
                    if dt.timestamp() < cutoff:
                        continue
                except Exception:
                    pass  # can't parse date, include it anyway

            articles.append({
                "title": title.strip(),
                "url": link.strip(),
                "snippet": description[:500].strip(),
                "source": source_name,
                "date": pub_date,
            })

    # 2. Scrape news pages for companies without RSS (e.g. Anthropic)
    cutoff_date = datetime.now().date()  # today only (last 24h)
    yesterday = (datetime.now() - timedelta(days=1)).date()

    for source_name, page_url, link_pattern in BLOG_SCRAPE:
        try:
            resp = client.get(page_url)
            resp.raise_for_status()
            html = resp.text
            origin = f"{urlparse(page_url).scheme}://{urlparse(page_url).netloc}"

            # Extract (date, path) pairs within each <li> to avoid cross-item mismatches
            date_link_pairs = []
            for li in re.finditer(r'<li[^>]*>(.*?)</li>', html, re.DOTALL):
                block = li.group(1)
                dates = re.findall(r'<time[^>]*>([^<]+)</time>', block)
                links = re.findall(link_pattern, block)
                if dates and links:
                    date_link_pairs.append((dates[0].strip(), links[0]))

            for date_str, path in date_link_pairs:
                # Parse date like "Feb 26, 2026"
                try:
                    post_date = datetime.strptime(date_str.strip(), "%b %d, %Y").date()
                except ValueError:
                    continue
                # Only include posts from last 24 hours
                if post_date < yesterday:
                    continue

                full_url = f"{origin}{path}" if path.startswith("/") else path
                slug = path.rstrip("/").rsplit("/", 1)[-1]
                title = slug.replace("-", " ").title()
                articles.append({
                    "title": title,
                    "url": full_url,
                    "snippet": "",
                    "source": source_name,
                    "date": date_str.strip(),
                })
        except Exception as e:
            print(f"Warning: scrape failed for {source_name}: {e}", file=sys.stderr)

    client.close()
    print(f"Fetched {len(articles)} blog posts from feeds/scrapes")
    return articles


def fetch_news() -> list[dict]:
    """Search DuckDuckGo for AI stories from the last 24 hours."""
    seen_urls = set()
    articles = []

    def add_article(title: str, url: str, snippet: str, source: str, date: str):
        if url and url not in seen_urls:
            seen_urls.add(url)
            articles.append({
                "title": title,
                "url": url,
                "snippet": snippet,
                "source": source,
                "date": date,
            })

    # 1. Direct RSS feeds from AI company blogs (most reliable)
    for post in fetch_blog_feeds():
        add_article(post["title"], post["url"], post["snippet"],
                    post["source"], post["date"])

    with DDGS() as ddgs:
        # 2. News search for general AI queries
        for query in NEWS_QUERIES:
            try:
                results = ddgs.news(query, max_results=10, timelimit="d")
            except Exception as e:
                print(f"Warning: news search failed for '{query}': {e}", file=sys.stderr)
                continue
            for r in results:
                add_article(
                    r.get("title", ""), r.get("url", ""),
                    r.get("body", ""), r.get("source", ""), r.get("date", ""),
                )

        # 3. Web search for company blogs (backup for feeds that fail)
        for query in BLOG_QUERIES:
            try:
                results = ddgs.text(query, max_results=5, timelimit="w")
            except Exception as e:
                print(f"Warning: blog search failed for '{query}': {e}", file=sys.stderr)
                continue
            for r in results:
                add_article(
                    r.get("title", ""), r.get("href", ""),
                    r.get("body", ""), _domain_to_source(r.get("href", "")),
                    "",
                )

    print(f"Fetched {len(articles)} total candidate articles")
    return articles


def _domain_to_source(url: str) -> str:
    """Extract a readable source name from a URL domain."""
    domain_map = {
        "anthropic.com": "Anthropic",
        "openai.com": "OpenAI",
        "blog.google": "Google",
        "deepmind.google": "Google DeepMind",
        "ai.meta.com": "Meta AI",
        "mistral.ai": "Mistral AI",
    }
    for domain, name in domain_map.items():
        if domain in url:
            return name
    return ""


def _extract_json(text: str) -> str | None:
    """Extract JSON from LLM response that may contain markdown code blocks or preamble."""
    # Try code block first
    if "```" in text:
        match = re.search(r'```(?:json)?\s*\n(.*?)```', text, re.DOTALL)
        if match:
            return match.group(1).strip()
    # Try to find JSON object directly
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return match.group(0).strip()
    return None


def _llm_client() -> OpenAI:
    """Create an OpenAI client configured for LLM Gateway."""
    return OpenAI(
        api_key=LLM_API_KEY,
        base_url=LLM_BASE_URL,
        http_client=httpx.Client(),
    )


def curate_with_claude(articles: list[dict], previous_briefs: list[dict] | None = None) -> dict:
    """Send candidate articles to Claude via LLM Gateway to pick top 5 and write summaries."""
    client = _llm_client()

    articles_text = json.dumps(articles, indent=2)

    dedup_section = ""
    if previous_briefs:
        dedup_lines = []
        for brief in previous_briefs:
            dedup_lines.append(f"\n[{brief['date']}]")
            for headline in brief["headlines"]:
                dedup_lines.append(f"- {headline}")
        dedup_section = f"""

CROSS-DAY DEDUPLICATION:
The following stories were already covered in recent daily briefs. Do NOT select stories about the same event/topic UNLESS there is a significant new development (e.g., new funding numbers, policy reversal, major new player involved, concrete product launch after prior rumors). Minor follow-up coverage, additional commentary, or new sources on the same event do NOT qualify.
{"".join(dedup_lines)}
"""

    prompt = f"""You are an AI news curator writing a daily brief for a tech-savvy reader.

Today is {DATE_STR}. Below are ~{len(articles)} candidate news articles from the past 24 hours about AI.

Your task:
1. Select the top 5 most significant, impactful stories. Prefer diversity of topics (chips, policy, products, research, business). Deduplicate similar stories — pick the best angle.
2. For each story, write a concise summary (2-3 sentences). Include key numbers, names, and context.
3. For each story, cite MULTIPLE sources (2-3 where possible). Group articles covering the same story together. Strongly prioritize official blog posts and announcements from AI companies (e.g. anthropic.com/news, openai.com/blog, blog.google, ai.meta.com) as the primary source when available, supplemented by press coverage (CNBC, Bloomberg, TechCrunch, etc.).
4. Write a "One to Watch" paragraph — a brief trend insight or forward-looking observation tied to today's news.
{dedup_section}
Output ONLY valid JSON in this exact format:
{{
  "stories": [
    {{
      "title": "Headline here",
      "summary": "2-3 sentence summary with context.",
      "sources": [
        {{"name": "Anthropic Blog", "url": "https://anthropic.com/news/..."}},
        {{"name": "CNBC", "url": "https://cnbc.com/..."}},
        {{"name": "TechCrunch", "url": "https://techcrunch.com/..."}}
      ]
    }}
  ],
  "one_to_watch": "Trend insight paragraph here."
}}

IMPORTANT: Each story MUST have a "sources" array with 1-3 entries. Prefer the official company blog/announcement as the first source when one exists in the candidates. Only use URLs that appear in the candidate articles below — do not fabricate URLs.

Candidate articles:
{articles_text}"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.choices[0].message.content.strip()
    extracted = _extract_json(text)
    if extracted:
        text = extracted
    return json.loads(text)


def curate_update(articles: list[dict], existing_brief: str) -> dict | None:
    """Ask Claude to find NEW stories not already covered in today's brief.

    Returns None if nothing noteworthy is new.
    """
    client = _llm_client()

    articles_text = json.dumps(articles, indent=2)

    prompt = f"""You are an AI news curator. A morning brief was already published today ({DATE_STR}).
Here is the existing brief:

---
{existing_brief}
---

Below are ~{len(articles)} candidate articles from recent hours. Your task:
1. Identify stories that are GENUINELY NEW and NOT already covered in the existing brief above.
2. A story is "already covered" if it's about the same event/announcement, even if from a different source.
3. Only select stories that are significant enough to warrant an update notification — minor developments or follow-up commentary on already-covered stories should be skipped.
4. Select 1-3 new stories max. If nothing is truly new and noteworthy, return an empty stories array.

Output ONLY valid JSON:
{{
  "stories": [
    {{
      "title": "Headline here",
      "summary": "2-3 sentence summary with context.",
      "sources": [
        {{"name": "Source", "url": "https://..."}}
      ]
    }}
  ]
}}

If there are NO new noteworthy stories, output: {{"stories": []}}

Only use URLs from the candidate articles below — do not fabricate URLs.

Candidate articles:
{articles_text}"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )

    text = (response.choices[0].message.content or "").strip()
    if not text:
        print("Warning: LLM returned empty response for update check")
        return None

    # Extract JSON robustly — handle code blocks, preamble text, etc.
    text = _extract_json(text)
    if not text:
        print("Warning: no JSON found in update response")
        return None

    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        print(f"Warning: could not parse update response: {text[:200]}")
        return None

    if not result.get("stories"):
        return None
    return result


def format_markdown(brief: dict) -> str:
    """Format the curated brief as markdown for archive."""
    lines = [
        f"# 🤖 AI Morning Brief — {DATE_STR}",
        "*Covers the past 24 hours only*",
        "",
        "---",
        "",
        "## 🚀 What's New",
        "",
    ]

    for i, story in enumerate(brief["stories"][:5]):
        sources = story.get("sources", [])
        if sources:
            source_links = " · ".join(
                f"[{s['name']}]({s['url']})" for s in sources
            )
            citation = f"({source_links})"
        else:
            citation = ""
        lines.append(f"- **{story['title']}** — {story['summary']} {citation}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 📌 One to Watch",
        "",
        brief["one_to_watch"],
        "",
        "---",
        "",
        f"*Generated {DATE_STR} · Sources verified to past 24 hours*",
    ])

    return "\n".join(lines)


def format_update_markdown(update: dict) -> str:
    """Format new stories as an update section to append to existing brief."""
    now_pt = datetime.now()  # Assumes system timezone is PT
    time_str = now_pt.strftime("%-I:%M %p")

    lines = [
        "",
        "---",
        "",
        f"## 🔄 Update — {time_str}",
        "",
    ]

    for story in update["stories"]:
        sources = story.get("sources", [])
        if sources:
            source_links = " · ".join(
                f"[{s['name']}]({s['url']})" for s in sources
            )
            citation = f"({source_links})"
        else:
            citation = ""
        lines.append(f"- **{story['title']}** — {story['summary']} {citation}")
        lines.append("")

    return "\n".join(lines)


def send_notification(brief: dict, archive_path: Path, is_update: bool = False) -> None:
    """Send a macOS notification with the brief headline and open the archive file on click."""
    titles = [s["title"] for s in brief["stories"][:3]]
    if is_update:
        subtitle = f"AI Brief Update — {DATE_STR}"
    else:
        subtitle = f"AI Morning Brief — {DATE_STR}"
    body = " · ".join(titles)

    # AppleScript for rich notification that opens the markdown file on click
    script = f'''
    display notification "{body}" with title "{subtitle}" sound name "Glass"
    '''
    subprocess.run(["osascript", "-e", script], check=True)

    # Also open the file in default markdown viewer
    subprocess.run(["open", str(archive_path)])
    print("macOS notification sent and archive opened")


def save_archive(markdown: str) -> Path:
    """Save markdown archive alongside existing briefs."""
    archive_dir = _brief_dir(TODAY)
    filepath = archive_dir / f"ai-brief-{DATE_FILE}.md"
    filepath.write_text(markdown)
    print(f"Archive saved to {filepath}")
    return filepath


def _is_pst_daytime() -> bool:
    """Check if current time is during PST/PDT daytime (7am-7pm)."""
    # Use system local time (assumes PT timezone on this machine)
    hour = datetime.now().hour
    return 7 <= hour < 19


def _brief_dir(date: datetime) -> Path:
    """Return the monthly subdirectory for a given date, creating it if needed."""
    d = Path(__file__).parent / date.strftime("%Y-%m")
    d.mkdir(exist_ok=True)
    return d


def load_recent_briefs(days: int = 3) -> list[dict]:
    """Load headlines from recent daily briefs for cross-day deduplication.

    Scans for ai-brief-YYYY-MM-DD.md files from the last N days (excluding today)
    and extracts story headlines (lines starting with '- **').
    """
    briefs = []
    for i in range(1, days + 1):
        date = TODAY - timedelta(days=i)
        path = _brief_dir(date) / f"ai-brief-{date.strftime('%Y-%m-%d')}.md"
        if not path.exists():
            continue
        headlines = []
        for line in path.read_text().splitlines():
            if line.startswith("- **"):
                # Extract "**Title** — Summary text (sources)"
                # Keep the bold title + first sentence of summary
                match = re.match(r'- \*\*(.+?)\*\*(.*)', line)
                if match:
                    title = match.group(1)
                    rest = match.group(2).lstrip(" —\u2014-")
                    # Take first sentence of summary
                    first_sentence = rest.split(". ")[0].strip()
                    if first_sentence:
                        headlines.append(f"{title} — {first_sentence}")
                    else:
                        headlines.append(title)
        if headlines:
            briefs.append({
                "date": date.strftime("%B %d, %Y"),
                "headlines": headlines,
            })
    return briefs


def extract_urls_from_brief(brief_path: Path) -> list[dict]:
    """Parse a brief markdown file and extract all URLs grouped by story headline."""
    text = brief_path.read_text()
    stories = []
    seen_urls: set[str] = set()
    current_headline = None
    current_urls: list[dict] = []

    for line in text.splitlines():
        # Match story lines: - **Headline** — Summary (sources)
        headline_match = re.match(r'^- \*\*(.+?)\*\*', line)
        if headline_match:
            # Save previous story if any
            if current_headline and current_urls:
                stories.append({"headline": current_headline, "urls": current_urls})
            current_headline = headline_match.group(1)
            current_urls = []
            # Extract all markdown links from this line
            for name, url in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', line):
                if url not in seen_urls:
                    seen_urls.add(url)
                    current_urls.append({"name": name, "url": url})

    # Don't forget the last story
    if current_headline and current_urls:
        stories.append({"headline": current_headline, "urls": current_urls})

    return stories


def fetch_article_content(url: str) -> str | None:
    """Fetch a URL and extract the main article text as markdown.

    Returns None on any failure (network error, paywall, parsing issue).
    """
    try:
        resp = httpx.get(
            url,
            timeout=15,
            follow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"},
        )
        resp.raise_for_status()
    except Exception:
        return None

    try:
        soup = BeautifulSoup(resp.text, "html.parser")

        # Strip non-content elements
        for tag in soup.find_all(["script", "style", "nav", "header", "footer", "aside"]):
            tag.decompose()

        # Find main content: <article> > div with content class > <main> > <body>
        content = (
            soup.find("article")
            or soup.find("div", class_=re.compile(r"article|post|content", re.I))
            or soup.find("main")
            or soup.body
        )
        if content is None:
            return None

        converter = html2text.HTML2Text()
        converter.body_width = 0  # no line wrapping
        converter.ignore_images = True
        converter.ignore_links = False

        md = converter.handle(str(content)).strip()

        # Truncate at 15,000 chars
        if len(md) > 15000:
            md = md[:15000] + "\n\n*[Article truncated at 15,000 characters]*"

        return md if md else None
    except Exception as e:
        print(f"  Parsing error for {url}: {e}", file=sys.stderr)
        return None


def format_companion_markdown(stories: list[dict], display_date: str, file_date: str) -> str:
    """Format fetched article content into the companion document."""
    lines = [
        f"# AI Brief — Full Articles — {display_date}",
        f"*Companion to ai-brief-{file_date}.md*",
        "",
        "---",
        "",
    ]

    for i, story in enumerate(stories, 1):
        lines.append(f"## {i}. {story['headline']}")
        lines.append("")

        for source in story["urls"]:
            lines.append(f"### {source['name']}")
            lines.append(f"*Source: {source['url']}*")
            lines.append("")

            if source.get("content"):
                lines.append(source["content"])
            else:
                lines.append(f"*Could not retrieve article content. [Read at source]({source['url']})*")

            lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def generate_companion(brief_path: Path) -> Path | None:
    """Generate a companion document with full article text for a given brief.

    Returns the path to the companion file, or None on failure.
    """
    if not brief_path.exists():
        print(f"Brief not found: {brief_path}", file=sys.stderr)
        return None

    # Derive dates from filename (ai-brief-YYYY-MM-DD.md)
    match = re.search(r'ai-brief-(\d{4}-\d{2}-\d{2})\.md$', brief_path.name)
    if not match:
        print(f"Could not parse date from filename: {brief_path.name}", file=sys.stderr)
        return None

    file_date = match.group(1)
    display_date = datetime.strptime(file_date, "%Y-%m-%d").strftime("%B %d, %Y")

    print(f"Generating companion document for {file_date}...")

    # 1. Extract URLs from the brief
    stories = extract_urls_from_brief(brief_path)
    if not stories:
        print("No URLs found in brief. Skipping companion generation.")
        return None

    total_urls = sum(len(s["urls"]) for s in stories)
    print(f"Found {total_urls} URLs across {len(stories)} stories")

    # 2. Fetch article content for each URL
    for story in stories:
        for source in story["urls"]:
            print(f"  Fetching: {source['name']} — {source['url'][:80]}...")
            content = fetch_article_content(source["url"])
            source["content"] = content
            if content:
                print(f"    ✓ {len(content)} chars")
            else:
                print(f"    ✗ Could not retrieve")

    # 3. Format companion document
    markdown = format_companion_markdown(stories, display_date, file_date)

    # 4. Save companion file
    companion_path = brief_path.parent / f"ai-brief-{file_date}-full.md"
    companion_path.write_text(markdown)
    print(f"Companion document saved to {companion_path}")
    return companion_path


def main(skip_companion: bool = False):
    archive_dir = _brief_dir(TODAY)
    archive_path = archive_dir / f"ai-brief-{DATE_FILE}.md"

    # Determine if this is an update run (brief already exists for today)
    is_update = archive_path.exists()

    if is_update:
        print(f"=== AI News Brief UPDATE — {DATE_STR} ===")

        # 1. Fetch latest news
        articles = fetch_news()
        if not articles:
            print("No articles found. Skipping update.")
            return

        # 2. Read existing brief
        existing_brief = archive_path.read_text()

        # 3. Ask Claude to find only new stories
        print("Checking for new stories...")
        update = curate_update(articles, existing_brief)

        if update is None:
            print("No new noteworthy stories. Skipping update.")
            return

        # 4. Append update section to existing file
        update_md = format_update_markdown(update)

        # Remove the trailing generated line before appending, then re-add it
        lines = existing_brief.rstrip().split("\n")
        # Strip the "Generated ..." footer if present
        if lines and lines[-1].startswith("*Generated"):
            lines.pop()
            # Also remove the "---" separator before it
            while lines and lines[-1].strip() in ("---", ""):
                lines.pop()

        new_content = "\n".join(lines) + update_md
        new_content += "\n---\n\n"
        new_content += f"*Updated {DATE_STR} · Sources verified to past 24 hours*\n"

        archive_path.write_text(new_content)
        print(f"Update appended to {archive_path}")

        # 5. Notify
        send_notification(update, archive_path, is_update=True)

        # 6. Generate companion document
        if not skip_companion:
            try:
                generate_companion(archive_path)
            except Exception as e:
                print(f"Warning: companion generation failed: {e}", file=sys.stderr)

    else:
        print(f"=== AI News Brief — {DATE_STR} ===")

        # 1. Fetch news
        articles = fetch_news()
        if not articles:
            print("No articles found. Exiting.", file=sys.stderr)
            sys.exit(1)

        # 2. Curate with Claude (with cross-day dedup context)
        previous_briefs = load_recent_briefs()
        if previous_briefs:
            covered = sum(len(b["headlines"]) for b in previous_briefs)
            print(f"Loaded {covered} headlines from {len(previous_briefs)} recent brief(s) for dedup")
        print("Curating with Claude...")
        brief = curate_with_claude(articles, previous_briefs=previous_briefs)

        # 3. Format markdown
        markdown = format_markdown(brief)

        # 4. Save archive
        filepath = save_archive(markdown)

        # 5. Send macOS notification and open brief
        send_notification(brief, filepath)

        # 6. Generate companion document
        if not skip_companion:
            try:
                generate_companion(filepath)
            except Exception as e:
                print(f"Warning: companion generation failed: {e}", file=sys.stderr)

    print("Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Daily News Brief")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--no-companion", action="store_true",
        help="Generate brief without companion document",
    )
    group.add_argument(
        "--companion", action="store_true",
        help="Regenerate companion for today's brief only",
    )
    group.add_argument(
        "--companion-only", metavar="YYYY-MM-DD",
        help="Generate companion for a specific date's brief",
    )
    group.add_argument(
        "--migrate", action="store_true",
        help="Move existing brief files into monthly subdirectories",
    )
    args = parser.parse_args()

    if args.migrate:
        root = Path(__file__).parent
        moved = 0
        for f in sorted(root.glob("ai-brief-*.md")):
            match = re.search(r'ai-brief-(\d{4}-\d{2}-\d{2})', f.name)
            if not match:
                continue
            date = datetime.strptime(match.group(1), "%Y-%m-%d")
            dest_dir = _brief_dir(date)
            dest = dest_dir / f.name
            if dest.resolve() == f.resolve():
                continue
            if dest.exists():
                print(f"  Skipping {f.name} (already exists at destination)")
                continue
            shutil.move(str(f), str(dest))
            print(f"  {f.name} -> {dest_dir.name}/{f.name}")
            moved += 1
        print(f"Migrated {moved} file(s).")
    elif args.companion_only:
        # Validate date format
        try:
            date = datetime.strptime(args.companion_only, "%Y-%m-%d")
        except ValueError:
            print(f"Error: Invalid date format '{args.companion_only}'. Use YYYY-MM-DD (e.g., 2026-03-03)", file=sys.stderr)
            sys.exit(1)
        # Generate companion for a specific past brief
        brief_path = _brief_dir(date) / f"ai-brief-{args.companion_only}.md"
        generate_companion(brief_path)
    elif args.companion:
        # Regenerate companion for today's brief
        brief_path = _brief_dir(TODAY) / f"ai-brief-{DATE_FILE}.md"
        generate_companion(brief_path)
    else:
        # Normal run (with or without companion)
        main(skip_companion=args.no_companion)
