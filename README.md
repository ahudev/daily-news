# Daily AI News Brief

A Python script that fetches, curates, and delivers a daily AI news digest via macOS notification.

## What it does

Each run:
1. Fetches AI news from RSS feeds (OpenAI, Google AI, DeepMind), Anthropic's blog, and DuckDuckGo news/web search
2. Sends candidates to Claude, which picks the top 5 stories, writes summaries, and adds a "One to Watch" trend insight
3. Saves a markdown brief to a monthly archive folder (`YYYY-MM/ai-brief-YYYY-MM-DD.md`)
4. Fetches full article text and saves a companion document (`*-full.md`)
5. Sends a macOS notification and opens the brief

If run again the same day, it checks for new stories and appends an update section instead of overwriting.

Cross-day deduplication: stories covered in the past 3 days are skipped unless there's a significant new development.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your API key
```

### Environment variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `LLM_GW_API_KEY` | Yes | — | API key for the LLM gateway |
| `LLM_GW_BASE_URL` | No | Salesforce internal gateway | OpenAI-compatible base URL |
| `LLM_GW_MODEL` | No | `claude-sonnet-4-6` | Model to use for curation |

## Usage

```bash
# Morning run — generate today's brief
python ai_news_brief.py

# Skip companion document generation
python ai_news_brief.py --no-companion

# Regenerate companion for today's brief
python ai_news_brief.py --companion

# Generate companion for a specific past brief
python ai_news_brief.py --companion-only 2026-03-01

# Migrate old brief files into monthly subdirectories
python ai_news_brief.py --migrate
```

## Output

Briefs are saved under monthly folders:

```
2026-03/
  ai-brief-2026-03-03.md       # Main brief
  ai-brief-2026-03-03-full.md  # Companion with full article text
```
