# AI Brief — Full Articles — March 03, 2026
*Companion to ai-brief-2026-03-03.md*

---

## 1. OpenAI Amends Pentagon AI Deal with New Surveillance Safeguards

### The New York Times
*Source: https://www.nytimes.com/2026/03/02/technology/openai-pentagon-deal-amended-surveillance.html*

*Could not retrieve article content. [Read at source](https://www.nytimes.com/2026/03/02/technology/openai-pentagon-deal-amended-surveillance.html)*

---

### Computerworld
*Source: https://www.computerworld.com/article/4139515/openai-says-its-us-defense-deal-is-safer-than-anthropics-but-is-it-2.html*

##  Legal experts say OpenAI’s deal with the US DoD offers little limitation beyond “all lawful use,” raising doubts about how enforceable its AI guardrails really are. 

Credit: JarTee / Shutterstock 

OpenAI has struck a deal to supply the US government with AI services, announcing it hours after US President Donald Trump’s [decision on Friday to ban its AI rival Anthropic](https://www.cio.com/article/4138822/trump-administration-bans-anthropic-escalating-clash-over-military-use-of-ai.html) from all US government contracts.

Sam Altman, CEO of OpenAI, said of the negotiation, “[It was definitely rushed, and the optics don’t look good,](https://x.com/sama/status/2027911640256286973)” in a post on X on Sunday.

Anthropic was banned for its refusal to let its product be used for mass surveillance of US citizens or in fully autonomous weapons; OpenAI said its deal contained the same limitations, raising questions about how it had managed to secure such concessions so quickly — or indeed whether it had secured them at all.

The US government wanted Anthropic to allow the use of its technology for all lawful purposes. Anthropic agreed, save for those [two exceptions](https://www.anthropic.com/news/statement-comments-secretary-war#:~:text=the%20mass%20domestic%20surveillance%20of%20Americans%20and%20fully%20autonomous%20weapons), and on Friday its intransigence got it banned.

On Saturday, OpenAI called for the government to offer deals to other AI companies on the same terms it had agreed to, saying in a blog post: “[We think our agreement has more guardrails](https://openai.com/index/our-agreement-with-the-department-of-war/) than any previous agreement for classified AI deployments, including Anthropic’s.”

## Redlining

“We have three main red lines that guide our work with the DoW, which are generally shared by several other frontier labs,” the company said, using the Department of Defense’s secondary name, the Department of War.

Those red lines, it said, are no use of its technology for mass domestic surveillance; no use of its technology to direct autonomous weapons systems, and no use of its technology for high-stakes automated decisions such as “social credit” systems.

So did OpenAI really succeed where Anthropic failed? And if so how?

OpenAI protects its red lines through “a more expansive, multi-layered approach,” it said in the Saturday blog post. “We retain full discretion over our safety stack, we deploy via cloud, cleared OpenAI personnel are in the loop, and we have strong contractual protections. This is all in addition to the strong existing protections in U.S. law.”

It cited the part of the contract offering those protections: “The Department of War may use the AI System for all lawful purposes, consistent with applicable law, operational requirements, and well-established safety and oversight protocols. The AI System will not be used to independently direct autonomous weapons in any case where law, regulation, or Department policy requires human control, nor will it be used to assume other high-stakes decisions that require approval by a human decisionmaker under the same authorities.”

That only imposes limits on the use of OpenAI technology to control autonomous weapons where the law or regulations forbid it; where laws and regulations are silent on the matter, it offers no protection.

“I’m not surprised that OpenAI has given DoW what DoW wanted. I am a little surprised that so many observers appear to be under the impression that the contract snippet OpenAI has published guarantees something significantly different from ‘all lawful use,’” wrote [Charlie Bullock](https://law-ai.org/team/charlie-bullock/), a senior research fellow at independent think tank Institute for Law and AI, said in a [post on X](https://x.com/CharlieBul58993/status/2028157898371613066).

As for mass domestic surveillance, the contract terms cited by OpenAI said, “For intelligence activities, any handling of private information will comply with the [Fourth Amendment](https://constitution.congress.gov/constitution/amendment-4/), the [National Security Act of 1947](https://history.state.gov/milestones/1945-1952/national-security-act) and the [Foreign Intelligence and Surveillance Act of 1978](https://bja.ojp.gov/program/it/privacy-civil-liberties/authorities/statutes/1286), [Executive Order 12333](https://www.nsa.gov/Signals-Intelligence/EO-12333/), and applicable DoD directives requiring a defined foreign intelligence purpose. The AI System shall not be used for unconstrained monitoring of U.S. persons’ private information as consistent with these authorities. The system shall also not be used for domestic law-enforcement activities except as permitted by the [Posse Comitatus Act](https://www.congress.gov/crs-product/R42669) and other applicable law.”

## OpenAI’s guardrails may not be enough

However, lawyers are not convinced that the contractual language that OpenAI quotes in the blog post is enough to stop the DoD from actually carrying out domestic mass surveillance in the US.

The contractual language that OpenAI revealed allow agencies like the NSA, which is a part of the DoD, to engage in bulk domestic metadata collection under existing legal powers, said [Pranesh Prakash](https://in.linkedin.com/in/praneshprakash), principal consultant at law and policy advisory firm Anekaanta.

Bullock wrote that he was unaware of a precise legal definition of mass domestic surveillance, saying there are things that a sufficiently advanced AI system could do that would be legal but would also qualify as mass domestic surveillance under at least some reasonable definitions of that term.

There are other ambiguities as well, Bullock noted, saying that the legal picture remains fuzzy, largely because OpenAI hasn’t published the full contract.

If the contract expressly limits surveillance or weapons related deployment, said [Anandaday Misshra](https://amlegals.com/our-founder/), founder of Amlegals, a law firm specializing in AI regulatory intelligence and data protection, “OpenAI can rely on standard contract law principles to enforce those limits, at least as between the parties.”

However, said Misshra, once the US government is involved, particularly through an entity like the DoD, OpenAI’s ability to prevent certain uses becomes more fragile: “National security carve-outs, classified programs, and sovereign immunity doctrines significantly weaken any attempt to challenge government use purely on ethical grounds. Courts have historically shown deference where national security is invoked, even when private contractors object,” he said.

There have been “similar tensions” in past disputes involving telecom surveillance and defense contracting, where companies relied on contractual language and internal governance but “ultimately had limited leverage once federal authorities asserted statutory powers,” he said.

Unfavorably for OpenAI, there is no clean precedent where a technology provider successfully blocked the federal government from using a tool for security or defense purposes once access was contractually granted, Misshra said, adding that national security exceptions would likely override softer commitments around ethical AI use in the case of a direct conflict.

The regulations around data protection don’t favor OpenAI’s position either, at least in their current form in the US, said Misshra.

“Unlike data protection and AI regimes in Europe, the United States does not yet have a binding federal AI law that would clearly prohibit military or intelligence applications, which means OpenAI is operating more on self-imposed policy than statutory protection,” Misshra said.

## A silver lining in the cloud deployment

There are some technical safeguards, OpenAI said. “This is a cloud-only deployment, with a safety stack that we run that includes these principles and others. We are not providing the DoW with ‘guardrails off’ or non-safety trained models, nor are we deploying our models on edge devices,” the company wrote in Saturday’s blog post. “Our deployment architecture will enable us to independently verify that these red lines are not crossed, including running and updating classifiers.”

Bullock wrote that, given OpenAI’s emphasis on the technical and operational protections, “[It makes sense to base your opinion of their decision on how much you trust the company](https://x.com/CharlieBul58993/status/2028159934156755216), their technical safeguards, and their in-the-loop personnel rather than on what the two paragraphs of their contract that they chose to publish say.”

Despite the promise of architectural control Misshra said disagreements like this between AI firms and the US government may set a precedent not for resistance, but for how tech companies negotiate guardrails.

“Expect future agreements to be more explicit on permitted use, audit rights, model versioning, and liability allocation. Ethical commitments will increasingly be embedded as contractual risk management tools rather than moral vetoes,” Misshra said.

This article first appeared on [CIO](https://www.cio.com/article/4139511/openai-says-its-us-defense-deal-is-safer-than-anthropics-but-is-it.html).

[Artificial Intelligence](https://www.computerworld.com/artificial-intelligence/)[Government IT](https://www.computerworld.com/government-it/)[Government](https://www.computerworld.com/government/)[Markets](https://www.computerworld.com/markets/)[Industry](https://www.computerworld.com/industry/)[Manufacturing Industry](https://www.computerworld.com/manufacturing-industry/)

SUBSCRIBE TO OUR NEWSLETTER 

###  From our editors straight to your inbox 

Get started by entering your email address below. 

Please enter a valid email address

Subscribe

---

### The Hindu
*Source: https://www.thehindu.com/sci-tech/technology/anthropics-resistance-to-the-us-department-of-defense-openais-entry-explained/article70698887.ece*

#  Anthropic’s resistance to the U.S. Department of Defence, OpenAI’s entry: Explained [Premium](/premium/)

## The Dario Amodei-led firm refused to cooperate with the U.S. government’s demands that the firm’s products be used in the deployment of autonomous strikes. The firm has been threatened with being designated as a “supply chain risk”

Updated  \- March 03, 2026 04:15 pm IST 

[Aroon Deep](https://www.thehindu.com/profile/author/aroon-deep-18354/)

READ LATER

[ SEE ALL ](https://www.thehindu.com/myaccount/?tab=bookmarks) Remove 

[](https://www.google.com/preferences/source?q=https://www.thehindu.com/)

Image used for representation purpose only. | Photo Credit: Reuters 

**The story so far** : The U.S. Department of Defence (styled as the [Department of War](https://www.thehindu.com/news/international/department-of-war-rebranding-pentagon-department-of-defence-trump-executive-order/article70018820.ece) under the second Trump administration) has entered into a public spat with the AI firm Anthropic, which makes the Claude AI product. The DoD has[ threatened to designate Anthropic](https://www.thehindu.com/news/international/anthropic-says-wont-give-us-military-unconditional-ai-use/article70682418.ece) a “supply chain risk,” dissuading a wide variety of firms that work with the US government from [patronising Anthropic’s products](https://www.thehindu.com/sci-tech/technology/what-to-know-about-the-clash-between-the-pentagon-and-anthropic-over-militarys-ai-use/article70693770.ece). ChatGPT maker OpenAI subsequently entered into the picture, obtaining an agreement it said was not radically different from what Anthropic wanted.

[ OpenAI amending deal with Pentagon, CEO Sam Altman says](https://www.thehindu.com/sci-tech/technology/openai-amending-deal-with-pentagon-ceo-sam-altman-says/article70697824.ece)

#### What is Claude?

[Claude is an AI chatbot](https://www.thehindu.com/sci-tech/technology/openai-anthropic-accuse-chinese-rivals-of-mass-ai-data-theft/article70669620.ece) that helps organisations and individual users create and modify code. Its Claude Code product has been received extraordinarily well due to its capabilities. [Claude Code is among the few AI products](https://www.thehindu.com/sci-tech/technology/saaspocalypse-why-did-anthropics-claude-cowork-plugins-spook-markets-the-hindu-explains/article70606600.ece) that is run with extremely powerful large language models (LLMs) while also supporting on-device creation and editing of tools, once it has access to a range of software libraries to work with.

The product is very compelling to the defence establishment because it can iterate on high-tech weapons and defence systems. Recruitment of programmers for these systems tends to be slow, as any critical weapons system is protected by several layers of secrecy, necessitating security clearances that can be time-consuming.

[ OpenAI, Anthropic accuse Chinese rivals of mass AI data theft](https://www.thehindu.com/sci-tech/technology/openai-anthropic-accuse-chinese-rivals-of-mass-ai-data-theft/article70669620.ece)

Claude Code has been a compelling proposition to the DoD as it likely allows them to iterate on programs that drive its technology quickly. While Claude Code does not perfectly execute programming tasks all the time, it performs well enough that a lot of development timelines have been shrunk in organisations that have deployed it widely, especially among personnel that are already experienced software developers.

#### Why did Anthropic clash with the DoD?

Anthropic was onboarded to the DoD as a part of a $200 million contract last June, which allowed the US government to use Claude’s services from dedicated infrastructure hosted by Amazon Web Services.

The issues between the firm and the DoD started on January 9, when defence secretary Pete Hegseth published a memorandum entitled “Accelerating America’s Military AI Dominance,” in which he called for the elimination of “blockers to data sharing, Authorizations to Operate (ATOs), test and evaluation and certification, contracting, hiring and talent management, and other policies that inhibit rapid experimentation and fielding”.

Anthropic has a much-publicised “constitution” for Claude that discourages the model from supporting widespread surveillance and enabling fully autonomous weaponry. Dario Amodei, the firm’s co-founder, insisted on strong language in the agreement between the DoD and Anthropic to bake in protections against domestic surveillance of US residents and enabling fully autonomous weaponry.

The firm was given until last Friday to relent and let the DoD have access to completely unrestricted access to its models. It refused, saying in a blog post that it would help the DoD transition to a new provider.

The DoD proceeded with the classification of Anthropic as a supply chain risk, a designation that is usually applied for firms that have such dodgy practices that their products can provide foreign adversaries a backdoor into critical systems. While this designation only disallows DoD suppliers and partners to not use Claude on systems that are dedicated to DoD, there are concerns that executives may lean on the side of caution and completely remove ties with Claude.

#### What is OpenAI’s agreement? How is it different?

OpenAI negotiated an agreement with the DoD that the former claims has the same protections against surveillance and fully autonomous weaponry that Anthropic sought. It is not fully clear why OpenAI was able to land this deal while Anthropic was cast out. “The Department of War may use the AI System for all lawful purposes, consistent with applicable law, operational requirements, and well-established safety and oversight protocols,” a portion of the agreement made public by OpenAI says.

“The AI System will not be used to independently direct autonomous weapons in any case where law, regulation, or Department policy requires human control, nor will it be used to assume other high-stakes decisions that require approval by a human decisionmaker under the same authorities.” Anthropic is reported to have sought greater clarity in the agreement’s legal language that would prohibit the use cases described above even if they were legalised.

“We think our red lines are more enforceable here because deployment is limited to cloud-only (not at the edge), keeps our safety stack working in the way we think is best, and keeps cleared OpenAI personnel in the loop,” OpenAI said in a statement. “We don’t know why Anthropic could not reach this deal, and we hope that they and more labs will consider it.”

Published \- March 03, 2026 03:27 pm IST

Read Comments 

  * Copy link 
  * [ Email ](mailto:?subject=Anthropic%E2%80%99s%20resistance%20to%20the%20U.S.%20Department%20of%20Defence%2C%20OpenAI%E2%80%99s%20entry%3A%20Explained&amp;body=Check%20out%20this%20link%20https%3A%2F%2Fwww.thehindu.com%2Fsci-tech%2Ftechnology%2Fanthropics-resistance-to-the-us-department-of-defense-openais-entry-explained%2Farticle70698887.ece)
  * Facebook 
  * Twitter 
  * Telegram 
  * LinkedIn 
  * WhatsApp 
  * Reddit 



READ LATER

[ SEE ALL ](https://www.thehindu.com/myaccount/?tab=bookmarks) Remove 

PRINT

###  Related Topics 

[ Artificial Intelligence ](https://www.thehindu.com/topic/artificial-intelligence/) / [ technology (general) ](https://www.thehindu.com/tag/1506-1461/) / [ USA ](https://www.thehindu.com/tag/413-244/)

---

## 2. AI-Powered Warfare Takes Center Stage as Operation Epic Fury Deploys AI at Scale in Iran

### NDTV
*Source: https://www.msn.com/en-in/news/world/how-operation-epic-fury-marked-first-large-scale-use-of-artificial-intelligence-in-war-explained/vi-AA1Xqy2r*

*Could not retrieve article content. [Read at source](https://www.msn.com/en-in/news/world/how-operation-epic-fury-marked-first-large-scale-use-of-artificial-intelligence-in-war-explained/vi-AA1Xqy2r)*

---

### Interesting Engineering
*Source: https://www.msn.com/en-us/news/world/how-ai-powered-warfare-in-iran-shrinks-the-distance-between-data-and-destruction/ar-AA1XrpF6*

*Could not retrieve article content. [Read at source](https://www.msn.com/en-us/news/world/how-ai-powered-warfare-in-iran-shrinks-the-distance-between-data-and-destruction/ar-AA1XrpF6)*

---

### Forbes
*Source: https://www.forbes.com/sites/digital-assets/2026/03/03/iran-war-an-oil-crisis-a-crypto-stress-test-and-an-ai-reckoning/*

*Could not retrieve article content. [Read at source](https://www.forbes.com/sites/digital-assets/2026/03/03/iran-war-an-oil-crisis-a-crypto-stress-test-and-an-ai-reckoning/)*

---

## 3. February 2026 Sets All-Time Startup Funding Record at $189 Billion, Driven Almost Entirely by AI Megadeals

### Crunchbase News
*Source: https://news.crunchbase.com/venture/record-setting-global-funding-february-2026-openai-anthropic/*

[Gené Teare](https://news.crunchbase.com/author/gene/) [@geneteare](https://twitter.com/@geneteare)

1 Shares

  * __ Email
  * __ Facebook
  * __ Twitter
  * __ LinkedIn



Crunchbase data shows global venture investment totaled $189 billion in February — the largest startup funding month on record — although 83% of capital raised went to just three companies. They include [OpenAI](https://www.crunchbase.com/organization/openai), which [raised $110 billion](https://news.crunchbase.com/venture/openai-raise-largest-ai-venture-deal-ever/), also in the largest round ever raised by a private, venture-backed company.

The record month for venture funding took place against the backdrop of a [trillion-dollar stock market drop](https://www.reuters.com/business/media-telecom/global-software-stocks-hit-by-anthropic-wake-up-call-ai-disruption-2026-02-04/) as AI compute and tooling unsettled leading public software companies.

All told, venture investment was up close to 780% year over year from the $21.5 billion raised by startups in February 2025.

OpenAI was not the only company to raise tens of billions of dollars last month. Its closest rival, [Anthropic](https://www.crunchbase.com/organization/anthropic), [raised $30 billion](https://news.crunchbase.com/ai/anthropic-raises-30b-second-largest-deal-all-time/), marking the third-largest venture round on record.

[Waymo](https://www.crunchbase.com/organization/waymo), [Alphabet](https://www.crunchbase.com/organization/alphabet)‘s self-driving division, raised $16 billion. Together, those three rounds totaled $156 billion, representing 83% of the global venture capital raised in February.

A further four companies each raised $1 billion or more last month: Tokyo-based semiconductor manufacturer [Rapidus;](https://www.crunchbase.com/organization/rapidus-110a) London-based self-driving platform [Wayve;](https://www.crunchbase.com/organization/wayve-9739) San Francisco-based AI for robotics [World Labs;](https://www.crunchbase.com/organization/world-labs) and Sunnyvale, California-based AI semiconductor company [Cerebras Systems](https://www.crunchbase.com/organization/cerebras-systems).

These massive rounds were led by strategic corporate investors, a host of private equity and alternative investors, as well as a few multistage venture investors and a government agency.

## Capital concentration

Seed-stage funding was down around 11% year over year with $2.6 billion raised, per Crunchbase data. Early-stage funding held up with $13.1 billion invested, up 47% year over year.

The trend of capital concentration was not only visible in the larger late-stage financings. Seed, Series A and Series B rounds’ median and average amounts have increased each year since 2024, and continued to do so through February.

## US dominated

U.S.-based startups raised $174 billion last month, Crunchbase data shows. That was the country’s largest percentage of global venture funding — 92%, and up from 59% a year earlier.

## AI and hardware surge

AI-related startups raised $171 billion in February, accounting for 90% of global venture funding. Other sectors that stood out include hardware-related startups dominated by autonomous-vehicle technology, semiconductors, robotics and networking products.

Two months into the year, the public and private markets are off to a very different start. Despite optimism that the IPO momentum we saw in 2025 would continue into 2026, public market volatility and uncertainty have stalled new offerings again. As a result, mobile marketing firm [Liftoff](https://www.crunchbase.com/organization/liftoff-io) and fintech brokerage firm [Clear Street](https://www.crunchbase.com/organization/clear-street-8e71) both withdrew their listings last month.

The private markets, by contrast, are on fire. Just a couple of months into the year, global venture funding has already topped 50% of the total invested in 2025.

## Related Crunchbase query:

  * [Global Venture Funding In 2026](https://www.crunchbase.com/discover/saved/global-venture-funding-in-2026/272d8783-dac9-4585-92d1-e10ad890d79e)



## Related reading:

  * [OpenAI’s New $110B Raise At A $840B Valuation Marks The Largest Venture Deal Ever](https://news.crunchbase.com/venture/openai-raise-largest-ai-venture-deal-ever/)
  * [Anthropic Raises $30B At $380B Valuation In Second-Largest Venture Funding Deal Of All Time](https://news.crunchbase.com/venture/openai-raise-largest-ai-venture-deal-ever/)



## Methodology

The data contained in this report comes directly from Crunchbase, and is based on reported data. Data reported is as of March 2, 2026.

Note that data lags are most pronounced at the earliest stages of venture activity, with seed funding amounts increasing significantly after the end of a quarter/year.

Please note that all funding values are given in U.S. dollars unless otherwise noted. Crunchbase converts foreign currencies to U.S. dollars at the prevailing spot rate from the date funding rounds, acquisitions, IPOs and other financial events are reported. Even if those events were added to Crunchbase long after the event was announced, foreign currency transactions are converted at the historic spot price.

## Glossary of funding terms

Seed and angel consists of seed, pre-seed and angel rounds. Crunchbase also includes venture rounds of unknown series, equity crowdfunding and convertible notes at $3 million (USD or as-converted USD equivalent) or less.

Early-stage consists of Series A and Series B rounds, as well as other round types. Crunchbase includes venture rounds of unknown series, corporate venture and other rounds above $3 million, and those less than or equal to $15 million.

Late-stage consists of Series C, Series D, Series E and later-lettered venture rounds following the “Series [Letter]” naming convention. Also included are venture rounds of unknown series, corporate venture and other rounds above $15 million. Corporate rounds are only included if a company has raised an equity funding at seed through a venture series funding round.

Technology growth is a private-equity round raised by a company that has previously raised a “venture” round. (So basically, any round from the previously defined stages.)

_Illustration:[Dom Guzman](https://www.domguzman.com/)_

Tags[AI](https://news.crunchbase.com/tag/ai/) [robotics](https://news.crunchbase.com/tag/robotics/) [seed](https://news.crunchbase.com/tag/seed/) [semiconductors](https://news.crunchbase.com/tag/semiconductors/) [startups](https://news.crunchbase.com/tag/startups/) [transportation](https://news.crunchbase.com/tag/transportation/) [unicorn](https://news.crunchbase.com/tag/unicorn/) [venture](https://news.crunchbase.com/tag/venture/)

Stay up to date with recent funding rounds, acquisitions, and more with the Crunchbase Daily. 

#### Featured

[ ](https://news.crunchbase.com/venture/global-funding-strong-q1-2025-ai-data/ "Q1 Global Startup Funding Posts Strongest Quarter Since Q2 2022 With A Third Going To Massive OpenAI Deal  ")

[Artificial intelligence](https://news.crunchbase.com/sections/ai/) • [Crypto](https://news.crunchbase.com/sections/fintech-ecommerce/crypto/) • [M&A](https://news.crunchbase.com/sections/ma/) • [Regional](https://news.crunchbase.com/sections/regional/) • [Seed funding](https://news.crunchbase.com/sections/seed/) • [Startups](https://news.crunchbase.com/sections/startups/) • [Venture](https://news.crunchbase.com/sections/venture/)

## [Q1 Global Startup Funding Posts Strongest Quarter Since Q2 2022 With A Third Going To Massive OpenAI Deal ](https://news.crunchbase.com/venture/global-funding-strong-q1-2025-ai-data/)

April 3, 2025

7 Min Read

####  **67.1K** Followers 

[ __ Follow us on Facebook 33.4K Followers ](https://www.facebook.com/crunchbase)

[ __ Follow us on Twitter 29K Followers ](https://twitter.com/crunchbasenews/)

[ __ Follow us on LinkedIn 4.7K Followers ](https://www.linkedin.com/company/3557157/)

#### CTA

Discover and act on private market opportunities with predictive company intelligence.

[GET STARTED](https://www.crunchbase.com/buy/select-product?utm_source=news&utm_medium=upsell&utm_campaign=sidebar-cta)

---

## 4. FDA Grants 'Breakthrough' Designation to Generative AI Chatbot for Surgical Recovery

### STAT News
*Source: https://www.statnews.com/2026/03/03/fda-breakthrough-designation-generative-ai-chatbot-recovryai/*

Pharma

Pharma February 27, 2026

### 

[ STAT Plus: Trump most-favored nation drug pricing deals end after three years for some companies ](https://www.statnews.com/2026/02/27/trump-drug-prices-pharma-mfn-deals-3-year-terms/)

---

## 5. GOP State Lawmakers Break with White House, Urge Trump to Stop Blocking State AI Laws

### The Hill
*Source: https://www.msn.com/en-us/news/other/gop-state-lawmakers-urge-white-house-to-halt-efforts-to-block-state-ai-laws/ar-AA1XqWnB*

*Could not retrieve article content. [Read at source](https://www.msn.com/en-us/news/other/gop-state-lawmakers-urge-white-house-to-halt-efforts-to-block-state-ai-laws/ar-AA1XqWnB)*

---

### The Stanford Review
*Source: https://stanfordreview.org/the-balkanization-of-american-ai-policy/*

## Table of Contents

In September, California Governor Gavin Newsom signed SB 53, which requires frontier labs to implement strict safety protocols, report catastrophic risks, and provide whistleblower protections, thereby establishing one of the first major AI regulations in the US. The predecessor to this bill, SB 1047, was vetoed by Newsom over a year ago due to its far-reaching provisions.

Even though California is the cradle of frontier AI innovation, other states have also begun crafting AI legislation. Over 1,000 AI-related bills [_were_](https://www.rila.org/blog/2025/09/ai-legislation-across-the-states-a-2025-end-of-ses?ref=stanfordreview.org) introduced across all 50 states in 2025, though only about 11% became law. States are scrambling to address visible, politically salient harms, such as synthetic media and consumer protection. These are important issues but risk hindering AI's strategic path as a catalyst for a new industrial revolution. On the other hand, the Trump administration [_signed_](https://www.businessinsider.com/trump-ai-executive-order-one-rule-state-regulations-2025-12?ref=stanfordreview.org) an executive order restricting state-level AI regulation in December, potentially risking future agility to adapt to unforeseen risks posed by AI.

Nevertheless, the scattered state-level approach to AI regulation misses the point of what's actually at stake. AI isn't just another tech sector where we can slap on standard consumer protection rules and move on. It has become a pillar of the American economy's future growth. Hyperscalers [_are_](https://www.goldmansachs.com/insights/articles/why-ai-companies-may-invest-more-than-500-billion-in-2026?ref=stanfordreview.org) pouring more than $500 billion into AI this year alone. Banks, asset managers, and pension funds [_have_](https://www.jpmorganchase.com/newsroom/press-releases/2025/jpmc-security-resiliency-initiative?ref=stanfordreview.org) all made trillion-dollar bets on AI infrastructure. If fragmented regulations kneecap AI development or push it overseas, we're not just hurting tech companies; we're exposing the broader economy to a financial crisis if the bets do not play out. 

If our regulatory response is fifty states pulling in different directions, we're handing over leadership in the century's defining technology. Recently, Chinese AI development has skyrocketed, with the gap between the [_capabilities_](https://artificialanalysis.ai/leaderboards/models?ref=stanfordreview.org) of American closed-source models and Chinese open-source alternatives [_narrowing_](https://hai.stanford.edu/policy/beyond-deepseek-chinas-diverse-open-weight-ai-ecosystem-and-its-policy-implications?ref=stanfordreview.org) rapidly. In December, for the first time in history, China [_outperformed_](https://papercopilot.com/paper-list/neurips-paper-list/neurips-2025-paper-list/?ref=stanfordreview.org) the US in the number of papers published at the top AI research conference, NeurIPS 2025 (based on affiliation of the first author). They closed a gap that [_was_](https://stanfordreview.org/we-trained-chinas-ai-researchers-now-we-risk-being-surpassed-in-ai-innovation/) nearly 5-to-1 in favor of America 5 years ago. We are not living in an era where California has consolidated AI dominance and is thinking about how to manage it, but in an arms race where it is unclear if the world will run on ChatGPT or Deepseek.

**I** **am not arguing against all AI regulations**. After all, poorly aligned AI systems have been [_linked_](https://www.nytimes.com/2026/01/07/technology/google-characterai-teenager-lawsuit.html?ref=stanfordreview.org) to multiple cases of teen suicides, and malicious actors have used them to [_launch_](https://www.anthropic.com/news/disrupting-AI-espionage?ref=stanfordreview.org) cyber attacks on critical infrastructure. It is an extremely powerful technology that could trigger an existential crisis if mismanaged.

But state-level regulation will not solve those problems. It would create a race to the bottom. States have every reason to compete for AI investment, which means they'll either slash regulations to attract companies or weaponize them to extract political favors. Imagine a law banning the storage of private data in Northern Virginia, where large swaths of American cloud infrastructure sit. The sunk cost of investment into immovable infrastructure prevents AI companies from migrating to other states. That kind of restriction wouldn't be about safety, but a leverage in political horse-trading.

AI demands we learn that lesson. It's too critical to American economic leadership, too embedded in financial stability, too central to global competition to manage through fifty different frameworks. A state legislator can score points by landing tech investments while adding requirements that hurt global competitiveness, or by gutting oversight entirely to win a bidding war. Neither serves the country. China is giving its AI sector a unified strategic direction. The winner in AI will shape economic power for generations. America needs a coherent strategy that does not hinder the power of its free market to overcome challenges, not a fragmented free-for-all.

---

## 6. Google Launches Gemini 3.1 Flash-Lite, Its Fastest and Most Cost-Efficient Model Yet

### Google AI Blog
*Source: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/*

# Gemini 3.1 Flash-Lite: Built for intelligence at scale

Mar 03, 2026

·

Share

[ x.com ](https://twitter.com/intent/tweet?text=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) [ Facebook ](https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/&title=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale) [ Mail ](mailto:?subject=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale&body=Check out this article on the Keyword:%0A%0AGemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale%0A%0AGemini 3.1 Flash-Lite is our fastest and most cost-efficient Gemini 3 series model yet.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)

Copy link

Get best-in-class intelligence for your highest-volume workloads. 

The Gemini Team

Read AI-generated summary 

## General summary

Gemini 3.1 Flash-Lite is now available in preview to developers via the Gemini API in Google AI Studio and for enterprises via Vertex AI. Priced at $0.25/1M input tokens and $1.50/1M output tokens, it's cost-efficient and faster than 2.5 Flash. Use 3.1 Flash-Lite for tasks like translation content moderation generating user interfaces and creating simulations.

Summaries were generated by Google AI. Generative AI is experimental. 

## Basic explainer

Google made a new AI model called Gemini 3.1 Flash-Lite. It's super fast and cheap to use, so more people can use it. This AI is good at things like translating languages and checking content. Some companies are already using it to solve tough problems because it's both smart and efficient.

Summaries were generated by Google AI. Generative AI is experimental. 

####  Explore other styles: 

  * General summary 
  * Basic explainer 



Share

[ x.com ](https://twitter.com/intent/tweet?text=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) [ Facebook ](https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/&title=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale) [ Mail ](mailto:?subject=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale&body=Check out this article on the Keyword:%0A%0AGemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale%0A%0AGemini 3.1 Flash-Lite is our fastest and most cost-efficient Gemini 3 series model yet.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)

Copy link

Your browser does not support the audio element.

Listen to article 

This content is generated by Google AI. Generative AI is experimental

[[duration]] minutes

Voice Speed

Voice

Speed 0.75X 1X 1.5X 2X

Today, we're introducing Gemini 3.1 Flash-Lite, our fastest and most cost-efficient Gemini 3 series model. Built for high-volume developer workloads at scale, 3.1 Flash-Lite delivers high quality for its price and model tier.

Starting today, 3.1 Flash-Lite is rolling out in preview to developers via the Gemini API in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview) and for enterprises via [Vertex AI](https://console.cloud.google.com/vertex-ai/studio/multimodal?mode=prompt&model=gemini-3.1-flash-lite-preview).

## Cost-efficiency without compromise

Priced at just $0.25/1M input tokens and $1.50/1M output tokens, 3.1 Flash-Lite delivers enhanced performance at a fraction of the cost of larger models. It outperforms 2.5 Flash with a 2.5X faster Time to First Answer Token and 45% increase in output speed, according to the [Artificial Analysis benchmark](https://artificialanalysis.ai/) while maintaining similar or better quality. This low latency is needed for high-frequency workflows, making it an ideal model for developers to build responsive, real-time experiences.

Gemini 3.1 Flash-Lite outperforms 2.5 Flash in speed and quality.

3.1 Flash-Lite achieves an impressive Elo score of 1432 on the [Arena.ai Leaderboard](http://arena.ai/leaderboard) and outperforms other models of similar tier across reasoning and multimodal understanding benchmarks, including 86.9% on GPQA Diamond and 76.8% on MMMU Pro–even surpassing larger Gemini models from prior generations like 2.5 Flash.

## Adaptive intelligence at scale for developers

Beyond its raw performance, Gemini 3.1 Flash-Lite comes standard with thinking levels in AI Studio and Vertex AI, giving developers the control and flexibility to select how much the model “thinks” for a task, which is critical for managing high-frequency workloads. 3.1 Flash-Lite can tackle tasks at scale, like high-volume translation and content moderation, where cost is a priority. And it can also handle more complex workloads where more in-depth reasoning is needed, like generating user interfaces and dashboards, creating simulations or following instructions.

3.1 Flash-Lite [instantly fills an e-commerce wireframe with hundreds](https://aistudio.google.com/apps/bundled/category_generator) of products in different categories.

3.1 Flash-Lite can [generate dynamic weather dashboards in real-time](https://aistudio.google.com/apps/bundled/weather_dashboard_agent), using live forecasts and historical data.

3.1 Flash-Lite creates a SaaS agent capable of [executing versatile, multi-step tasks for a business](https://aistudio.google.com/apps/bundled/versatile_execution_agent).

3.1 Flash-Lite can analyze and sort large numbers of content like images quickly.

Early-access developers on AI Studio and Vertex AI, and companies like Latitude, Cartwheel and Whering are already using 3.1 Flash-Lite to solve complex problems at scale. Early testers highlighted 3.1 Flash-Lite’s efficiency and reasoning capabilities, saying it can handle complex inputs with the precision of a larger-tier model, plus follow instructions and maintain adherence.

We look forward to seeing what you build with 3.1 Flash-Lite and the rest of the Gemini 3 series models.

##  Get more stories from Google in your inbox. Get more stories from Google in your inbox.

Email address 

Your information will be used in accordance with [Google's privacy policy.](https://policies.google.com/privacy)

Subscribe 

Done. Just one step more. 

Check your inbox to confirm your subscription. 

You are already subscribed to our newsletter.

You can also subscribe with a different email address . 

POSTED IN:

---

### Google DeepMind
*Source: https://deepmind.google/blog/gemini-3-1-flash-lite-built-for-intelligence-at-scale/*

# Gemini 3.1 Flash-Lite: Built for intelligence at scale

Mar 03, 2026

·

Share

[ x.com ](https://twitter.com/intent/tweet?text=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) [ Facebook ](https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/&title=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale) [ Mail ](mailto:?subject=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale&body=Check out this article on the Keyword:%0A%0AGemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale%0A%0AGemini 3.1 Flash-Lite is our fastest and most cost-efficient Gemini 3 series model yet.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)

Copy link

Get best-in-class intelligence for your highest-volume workloads. 

The Gemini Team

Read AI-generated summary 

## General summary

Gemini 3.1 Flash-Lite is now available in preview to developers via the Gemini API in Google AI Studio and for enterprises via Vertex AI. Priced at $0.25/1M input tokens and $1.50/1M output tokens, it's cost-efficient and faster than 2.5 Flash. Use 3.1 Flash-Lite for tasks like translation content moderation generating user interfaces and creating simulations.

Summaries were generated by Google AI. Generative AI is experimental. 

## Basic explainer

Google made a new AI model called Gemini 3.1 Flash-Lite. It's super fast and cheap to use, so more people can use it. This AI is good at things like translating languages and checking content. Some companies are already using it to solve tough problems because it's both smart and efficient.

Summaries were generated by Google AI. Generative AI is experimental. 

####  Explore other styles: 

  * General summary 
  * Basic explainer 



Share

[ x.com ](https://twitter.com/intent/tweet?text=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) [ Facebook ](https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) [ LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/&title=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale) [ Mail ](mailto:?subject=Gemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale&body=Check out this article on the Keyword:%0A%0AGemini%203.1%20Flash-Lite%3A%20Built%20for%20intelligence%20at%20scale%0A%0AGemini 3.1 Flash-Lite is our fastest and most cost-efficient Gemini 3 series model yet.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)

Copy link

Your browser does not support the audio element.

Listen to article 

This content is generated by Google AI. Generative AI is experimental

[[duration]] minutes

Voice Speed

Voice

Speed 0.75X 1X 1.5X 2X

Today, we're introducing Gemini 3.1 Flash-Lite, our fastest and most cost-efficient Gemini 3 series model. Built for high-volume developer workloads at scale, 3.1 Flash-Lite delivers high quality for its price and model tier.

Starting today, 3.1 Flash-Lite is rolling out in preview to developers via the Gemini API in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview) and for enterprises via [Vertex AI](https://console.cloud.google.com/vertex-ai/studio/multimodal?mode=prompt&model=gemini-3.1-flash-lite-preview).

## Cost-efficiency without compromise

Priced at just $0.25/1M input tokens and $1.50/1M output tokens, 3.1 Flash-Lite delivers enhanced performance at a fraction of the cost of larger models. It outperforms 2.5 Flash with a 2.5X faster Time to First Answer Token and 45% increase in output speed, according to the [Artificial Analysis benchmark](https://artificialanalysis.ai/) while maintaining similar or better quality. This low latency is needed for high-frequency workflows, making it an ideal model for developers to build responsive, real-time experiences.

Gemini 3.1 Flash-Lite outperforms 2.5 Flash in speed and quality.

3.1 Flash-Lite achieves an impressive Elo score of 1432 on the [Arena.ai Leaderboard](http://arena.ai/leaderboard) and outperforms other models of similar tier across reasoning and multimodal understanding benchmarks, including 86.9% on GPQA Diamond and 76.8% on MMMU Pro–even surpassing larger Gemini models from prior generations like 2.5 Flash.

## Adaptive intelligence at scale for developers

Beyond its raw performance, Gemini 3.1 Flash-Lite comes standard with thinking levels in AI Studio and Vertex AI, giving developers the control and flexibility to select how much the model “thinks” for a task, which is critical for managing high-frequency workloads. 3.1 Flash-Lite can tackle tasks at scale, like high-volume translation and content moderation, where cost is a priority. And it can also handle more complex workloads where more in-depth reasoning is needed, like generating user interfaces and dashboards, creating simulations or following instructions.

3.1 Flash-Lite [instantly fills an e-commerce wireframe with hundreds](https://aistudio.google.com/apps/bundled/category_generator) of products in different categories.

3.1 Flash-Lite can [generate dynamic weather dashboards in real-time](https://aistudio.google.com/apps/bundled/weather_dashboard_agent), using live forecasts and historical data.

3.1 Flash-Lite creates a SaaS agent capable of [executing versatile, multi-step tasks for a business](https://aistudio.google.com/apps/bundled/versatile_execution_agent).

3.1 Flash-Lite can analyze and sort large numbers of content like images quickly.

Early-access developers on AI Studio and Vertex AI, and companies like Latitude, Cartwheel and Whering are already using 3.1 Flash-Lite to solve complex problems at scale. Early testers highlighted 3.1 Flash-Lite’s efficiency and reasoning capabilities, saying it can handle complex inputs with the precision of a larger-tier model, plus follow instructions and maintain adherence.

We look forward to seeing what you build with 3.1 Flash-Lite and the rest of the Gemini 3 series models.

##  Get more stories from Google in your inbox. Get more stories from Google in your inbox.

Email address 

Your information will be used in accordance with [Google's privacy policy.](https://policies.google.com/privacy)

Subscribe 

Done. Just one step more. 

Check your inbox to confirm your subscription. 

You are already subscribed to our newsletter.

You can also subscribe with a different email address . 

POSTED IN:

---

### IFLScience
*Source: https://www.iflscience.com/humanitys-last-exam-reveals-how-accurate-ai-actually-is-chatbots-might-want-to-look-away-now-82729*

Artificial intelligence (AI) researchers have created what they are calling "Humanity's Last Exam" in an attempt to benchmark the progress of large language models (LLMs). Looking at the performance of top current models, there is a clear frontrunner.

The rest of this article is behind a paywall. Please sign in or subscribe to access the full content.

Though there are still [plenty of problems](https://www.iflscience.com/todays-top-ai-went-up-against-expert-mathematicians-it-lost-badly-76919) with LLMs if you are a fan of [accuracy](https://www.iflscience.com/can-we-legally-require-ai-chatbots-to-tell-the-truth-75461) or [ethics](https://www.iflscience.com/ai-chatbots-found-to-violate-ethical-standards-when-it-comes-to-mental-health-discussions-81296), there's no denying they have progressed astonishingly quickly over the last decade. The Turing test, created by renowned mathematician and computer scientist Alan Turing in 1950, looks to see if a computer can fool a human into believing that it too is an ordinary human being. That has likely been [beaten by LLMs](https://www.iflscience.com/chatgpt-might-have-passed-the-turing-test-new-study-suggests-74711).

"Participants in our experiment were no better than chance at identifying GPT-4 after a five minute conversation, suggesting that current AI systems are capable of deceiving people into believing that they are human,” a [2025 paper](https://dl.acm.org/doi/10.1145/3715275.3732108) explains. “The results here likely set a lower bound on the potential for deception in more naturalistic contexts where, unlike the experimental setting, people may not be alert to the possibility of deception or exclusively focused on detecting it."

While beating the Turing test [doesn't mean that AI is conscious](https://www.iflscience.com/how-can-we-tell-if-artificial-intelligence-is-conscious-70460), it does mean that the test may be a little useless to AI researchers. There are other ways of assessing their performance, such as the Massive Multitask Language Understanding benchmark, which tests the "knowledge" of LLMs – or their ability to put forward the correct answer when prompted – across a broad range of subjects. But this too is no longer cutting it.

"Benchmarks are important tools for tracking the rapid advancements in large language model (LLM) capabilities," the creators of Humanity's Last Exam (HLE) explain in their paper. "However, benchmarks are not keeping pace in difficulty: LLMs now achieve over 90% accuracy on popular benchmarks like MMLU, limiting informed measurement of state-of-the-art LLM capabilities."

The new benchmark contains 2,500 questions across a broad range of subjects, including science and the humanities, which have been developed by subject experts from around the world. Each question is designed with an unambiguous answer that can be automatically graded, and, crucially, with answers that cannot be answered easily by retrieving them via the Internet. In general, the questions were designed to require graduate-level knowledge of the subject area. The models were also asked to suggest how confident they were of each answer, so that they could compare it to how well they performed.

"Among the diversity of questions in the benchmark, HLE emphasizes world-class mathematics problems aimed at testing deep reasoning skills broadly applicable across multiple academic areas," the team adds, with math making up 41 percent of the questions.

The team evaluated current models of LLMs against Humanity's Last Exam to test the effectiveness of the exam as well as the models taking it. So, how did they do? Not great. 

"All frontier models achieve low accuracy on HLE, highlighting substantial room for improvement in narrowing the gap between current LLMs and expert-level academic capabilities on closed-ended questions," the team writes, adding, "these low scores are partially by design the dataset collection process attempts to filter out questions that existing models can answer correctly."

As well as performing poorly, the team found that many of the LLMs were overconfident in being correct in their answers.

"The stated confidence of a well-calibrated model should match its actual accuracy," the team explains, "for example, achieving 50% accuracy on questions, in which it claims 50% confidence."

GPT-4o, for example, achieved an accuracy rating of around 2.7 percent, a calibration error of 89 percent in this overconfident model. Later models performed better, with Gemini 2.5 Pro being accurate around 22 percent of the time, and GPT-5 around 25 percent of the time. These models were still too confident, however, with a calibration error of 72 percent and 50 percent, respectively. 

In updated tests published to the Humanity's Last Exam website, Gemini's 3.1 Pro model achieved 45.9 percent accuracy, with a 50.3 percent calibration error, taking the spot as the top-performing model. Chat GPT-5.2 also improved, with 36.6 percent accuracy and a slightly higher calibration error of 55.1 percent.

That may not sound great, but given that they were searching specifically for new ways to benchmark the models, this isn't a bad thing.

"Without accurate assessment tools, policymakers, developers and users risk misinterpreting what AI systems can actually do,” Dr Tung Nguyen, Instructional Associate Professor of Computer Science and Engineering at Texas A&M University College of Engineering, said in a [statement](https://stories.tamu.edu/news/2026/02/25/dont-panic-humanitys-last-exam-has-begun/). "Benchmarks provide the foundation for measuring progress and identifying risks."

The exam is [publicly available](https://lastexam.ai/), though the answers are hidden from any AI thinking of simply Googling the correct response.

The study is published in [Nature](https://doi.org/10.1038/s41586-025-09962-4).

* * *

ORIGINALLY PUBLISHED9 hours ago

Written by [James Felton](/james-felton)

[Edited](/editorial-mission-statement)by[Holly Large](/holly-large)

Discuss (2 CommentS)

Discuss (2 CommentS)

SHARE

FOLLOW

[](https://news.google.com/publications/CAAqBwgKMMDnygsw8ILiAw?hl=en-GB&gl=GB&ceid=GB%3Aen)[](https://www.google.com/preferences/source?q=iflscience.com)

Add us as a Google preferred source to see more of our trusted coverage in Search

---

## 7. Block Cuts 40% of Staff, Citing AI — Is It a Bellwether for Broader AI-Driven Layoffs?

### American Banker
*Source: https://www.americanbanker.com/payments/news/is-block-the-first-domino-for-ai-spurred-layoffs*

[Layoffs](https://www.americanbanker.com/tag/layoffs)

#  Is Block the first domino for AI-spurred layoffs? 

By  [Joey Pizzolato](https://www.americanbanker.com/author/joey-pizzolato)

CloseText

[ ](https://www.americanbanker.com/author/joey-pizzolato) |  [About Joey](https://www.americanbanker.com/author/joey-pizzolato)  
---|---  
[ twitter ](https://twitter.com/joeypizzolato) |  [joeypizzolato](https://twitter.com/joeypizzolato)  
[ mailto ](mailto: joey.pizzolato@arizent.com) |  [joey.pizzolato@arizent.com](mailto: joey.pizzolato@arizent.com)  
[ linkedin ](https://www.linkedin.com/in/joey-pizzolato-02178325) |  [joey-pizzolato-02178325](https://www.linkedin.com/in/joey-pizzolato-02178325)  
  
March 02, 2026, 3:40 p.m. EST  5 Min Read

  * [ Facebook ](https://www.facebook.com/dialog/share?app_id=4725977577498274&display=popup&href=https%3A%2F%2Fwww.americanbanker.com%2Fpayments%2Fnews%2Fis-block-the-first-domino-for-ai-spurred-layoffs)
  * [ Twitter ](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.americanbanker.com%2Fpayments%2Fnews%2Fis-block-the-first-domino-for-ai-spurred-layoffs&text=Is%20Block%20the%20first%20domino%20for%20AI-spurred%20layoffs%3F)
  * [ LinkedIn ](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fwww.americanbanker.com%2Fpayments%2Fnews%2Fis-block-the-first-domino-for-ai-spurred-layoffs&mini=true&title=Is%20Block%20the%20first%20domino%20for%20AI-spurred%20layoffs%3F&summary=Block%20last%20week%20cut%2040%25%20of%20its%20staff%20and%20attributed%20the%20layoffs%20to%20artificial%20intelligence%2C%20leaving%20many%20to%20wonder%20whether%20Jack%20Dorsey%27s%20payments%20company%20was%20a%20bellwether%20for%20widespread%20AI-driven%20layoffs%2C%20or%20a%20one-off.%20&source=American%20Banker)
  * [ Email ](mailto:?body=Is%20Block%20the%20first%20domino%20for%20AI-spurred%20layoffs%3F%0A%0Ahttps%3A%2F%2Fwww.americanbanker.com%2Fpayments%2Fnews%2Fis-block-the-first-domino-for-ai-spurred-layoffs%0A%0ABlock%20last%20week%20cut%2040%25%20of%20its%20staff%20and%20attributed%20the%20layoffs%20to%20artificial%20intelligence%2C%20leaving%20many%20to%20wonder%20whether%20Jack%20Dorsey%27s%20payments%20company%20was%20a%20bellwether%20for%20widespread%20AI-driven%20layoffs%2C%20or%20a%20one-off.%20)



Cole Burston/Bloomberg

  * **Key insights** : Block last week cut 40% of its staff and attributed the layoffs to artificial intelligence, leaving many to wonder whether Jack Dorsey's payments company was a bellwether for widespread AI-driven layoffs. 
  * **What's at stake** : Forrester Research predicts that AI automation will take 6.1% of U.S. jobs by 2030. 
  * **Expert quote** : "The most severe AI-driven headcount reductions will inevitably target the operational layers that manage friction rather than generate revenue," Eric Grover, principal of Intrepid Ventures, told American Banker. 



It was the combination of "layoffs" and "artificial intelligence" that stoked broader concern for an AI-driven shock to the labor market, leaving many to wonder whether Jack Dorsey's payments company Block was a bellwether for mass AI-fueled firings, or merely a one-off. 

Processing Content

Block last week cut 40% of its staff and attributed the layoffs to artificial intelligence. The layoffs came with a prediction: More companies will follow suit. 

"Within the next year, I believe the majority of companies will reach the same conclusion and make similar structural changes," Block CEO Jack Dorsey wrote in the company's fourth-quarter [_shareholder letter_](https://s29.q4cdn.com/628966176/files/doc_financials/2025/q4/Q4-2025-Shareholder-Letter_Block.pdf). Markets were receptive – as of midday Monday, shares of Block, which trade on the New York Stock Exchange, had increased more than 17% since market close on Feb. 26, when Block reported its fourth-quarter earnings and announced the layoffs.   


## AI takeover, or a traditional downsizing?

But analysts and industry experts [_have been hesitant_](https://www.americanbanker.com/news/feds-barr-outlines-ai-risks-to-finance-labor-market) to hail the move as a catalyst for widespread reductions in workforce, noting many fintechs added jobs during the e-commerce wave that accompanied the COVID-19 pandemic. 

"Wall Street clearly loves the AI narrative, and there's no question the technology will drive meaningful productivity gains across customer service, dispute resolution, and junior engineering," Eric Grover, principal at Intrepid Ventures, told American Banker. "That said, I'm skeptical that AI is the primary catalyst for Block cutting 4,000 jobs. The company has been performing well, so there wasn't a wave of external pressure to reduce headcount. But if leadership sees a need, acting early is better than waiting."

Prior to the cuts, Block's workforce had ballooned from roughly 3,800 employees in 2019 to nearly 13,000 by 2023, leading to a self-imposed cap of 12,000 employees that same year. Last March, [_Block cut 931 people_](https://www.americanbanker.com/payments/news/block-lays-off-8-of-staff-western-union-adopts-ai) , or about 8% of its staff, and in January 2024, laid off approximately 1,000 employees, or roughly 8% of its staff.

"This looks far more like a long‑overdue correction to a massive pandemic‑era hiring binge," Grover said. "While Block's cuts are severe by percentage, the absolute numbers don't touch the real records. They pale in comparison to IBM laying off 60,000 employees in 1993. Even more recently, UPS eliminated 48,000 roles, and Amazon is currently in the process of laying off 30,000 corporate employees."

Sanjay Sakhrani, a senior analyst at Keefe, Bruyette and Woods, also said that the layoffs at Block were likely unique to the company, rather than the proverbial canary in a coal mine. 

"AI-driven job displacement will be an evolution, not a revolution," Sakhrani said. "While AI will inevitably reshape the work force over time, we think the big, bold moves like the one made by Block are unique to its circumstances and leadership, and are likely to be the exception rather than the norm over the intermediate period." 

Consultancy firms have been split on AI's ultimate impact on the labor market. Forrester Research said in January that AI and automation would take about 6% of U.S. jobs by 2030. Gartner, on the other hand, said AI would produce more jobs than it destroyed by 2028.

The narrative that AI will [_wipe out a majority of jobs_](https://www.americanbanker.com/payments/news/ai-and-career-growth-what-payments-executives-should-know) is one that is easy to lean into, Sakhrani said. "We do believe this is a trend worth watching carefully. AI is clearly improving productivity, automating certain workflows, and reducing the need for some repetitive or lower-value tasks. Over time, that will inevitably reshape parts of the workforce. However, reshaping is not the same as collapsing."   


## Leading by example

There is some concern that Block is setting a precedent for other companies looking to capitalize on the promise of artificial intelligence, Aaron Press, a research director at IDC, told American Banker. 

"I do have some worries about the message the stock bump sends to other companies in the industry," Press said. "While I'm willing to believe Block is likely far enough down an AI deployment path to have at least some understanding of the impact, I fear that other companies will cut first and claim that AI will make up the difference, all while having no real idea how that's going to be accomplished." 

Block is not the first company to attribute AI to staff cuts. Klarna's CEO Sebastian Siemiatkowski said in August 2024 that AI had contributed to cutting its headcount to about 3,800 employees, down from about 5,000 in August 2023. That reduction largely came through attrition, rather than layoffs, a company spokesperson [_previously told American Banker_](https://www.americanbanker.com/payments/list/klarna-predicts-ais-toll-on-jobs-indias-payment-rail-boosts-walmart). In the spring of 2025, Klarna began piloting a flexible, gig-style model to onboard remote human agents in addition to its AI to ensure there would always be a person available to handle inquiries if a customer wanted.

But that doesn't mean there aren't areas of payments ripe for AI-powered automation. 

"Looking across merchant acquirers, processors, payment facilitators, networks, and issuers, the most severe AI-driven headcount reductions will inevitably target the operational layers that manage friction rather than generate revenue," Grover said. 

Back-office reengineering with AI is the low-hanging fruit, Richard Crone, CEO of Crone Consulting, told American Banker. 

"That's what you're seeing [with Block]," Crone said. "AI has been around in earnest for about two years now, and it has been shadowing workers and workflows. Workers have really been skiing with AI right next to them, and now we are ready to pull out of manual labor and depend at least for 30% to 50% of those labor intensive functions on AI. That's what you're seeing." 

For payment companies, including payment facilitators like Block, Adyen, Stripe and PayPal, almost a quarter of costs are associated with customer support, disputes and charge-backs, all of which are historically labor intensive and could be streamlined with assistance from AI. 

Know-your-customer and anti-money-laundering compliance are also great use cases for AI, Crone said. 

"Underwriting, merchant onboarding, digital account opening, risk, fraud, AML and compliance require manual review for roughly 40% of approvals, but AI is cutting those cycles in half, permanently resetting cost per approved account and reinforcing the merchant of record automation model invented by PayPal and followed by all other payment facilitators," Crone said. 

[Joey Pizzolato](https://www.americanbanker.com/author/joey-pizzolato)

Reporter, American Banker 

  * [ ](https://www.americanbanker.com/author/joey-pizzolato)


  * [ twitter ](https://twitter.com/joeypizzolato)
  * [ mailto ](mailto: joey.pizzolato@arizent.com)
  * [ linkedin ](https://www.linkedin.com/in/joey-pizzolato-02178325)

---

## 8. OpenAI Quietly Releases GPT-5.3 Instant

### OpenAI
*Source: https://openai.com/index/gpt-5-3-instant*

*Could not retrieve article content. [Read at source](https://openai.com/index/gpt-5-3-instant)*

---

### OpenAI System Card
*Source: https://openai.com/index/gpt-5-3-instant-system-card*

*Could not retrieve article content. [Read at source](https://openai.com/index/gpt-5-3-instant-system-card)*

---

## 9. Anthropic's Claude Confirmed in Active Use in Iran War — Despite Company's Pentagon Standoff

### CBS News
*Source: https://www.msn.com/en-us/news/world/anthropics-claude-ai-being-used-in-iran-war-by-us-military-sources-say/ar-AA1Xsljt*

*Could not retrieve article content. [Read at source](https://www.msn.com/en-us/news/world/anthropics-claude-ai-being-used-in-iran-war-by-us-military-sources-say/ar-AA1Xsljt)*

---

### Associated Press
*Source: https://apnews.com/article/anthropic-pentagon-openai-claude-chatgpt-military-ai-b2bbcf5fda3f27353eae1e0eb7ab07b6*

SECTIONS

[Iran war](https://apnews.com/hub/iran) [Russia-Ukraine war](https://apnews.com/hub/russia-ukraine) [Español](https://apnews.com/hub/noticias) [China](https://apnews.com/hub/china) [Asia Pacific](https://apnews.com/hub/asia-pacific) [Latin America](https://apnews.com/hub/latin-america) [Europe](https://apnews.com/hub/europe) [Africa](https://apnews.com/hub/africa)

TOP STORIES

  * [LIVE Trump says ‘someone from within’ Iran may be best choice to take power](https://apnews.com/live/iran-war-israel-trump-03-03-2026)
  * [Trump takes unconventional approach to communicating to the public about war in Iran](https://apnews.com/article/iran-trump-administration-media-communication-2aeb11fcfef4138c045be71fb7216792)
  * [Israel steps up airstrikes in Tehran, as Iran widens its response across the region](https://apnews.com/article/iran-israel-us-03-03-2026-8755877b603e46ed3df8107689c1ee23)



Newsletters

[ The Morning Wire Our flagship newsletter breaks down the biggest headlines of the day. ](/newsletters?id=Morning+Wire+Subscribers) [ The Afternoon Wire Get caught up on what you may have missed throughout the day. ](/newsletters?id=Afternoon+Wire)

[See All Newsletters](/newsletters)

---
