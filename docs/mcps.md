# MCP Tools

MCP (Model Context Protocol) tools give your AI agent the ability to research topics in real time — searching the web, checking Reddit, and more.

---

## What Are MCPs?

MCPs are plugins that connect your AI tool to external services. They let the AI actually search the internet, check Reddit, and pull live data instead of relying on its training knowledge.

Without MCPs, the AI can still write posts but can't research what's currently trending.

---

## Recommended Approach: Built-in Web Search + Engine

Most AI tools (Kiro, Claude Code, Cursor) have built-in web search and page fetching. Post-kit includes a **web research engine** (`engine/core/web-research.md`) that teaches the agent HOW to search effectively — multi-angle queries, source triage, progressive depth, and citation-backed synthesis.

This gives you:
- Zero external dependencies for search
- No API keys or rate limits
- Smarter research through better methodology, not more tools
- Works across any AI tool with web access

The web research engine activates automatically during the pipeline's Research step.

---

## Universal MCPs (Recommended for Everyone)

These work for any niche:

### Reddit
**What it does:** Checks subreddit posts (hot, rising, top) for what your audience is talking about.
**Why you need it:** Real-time pulse on your community. Cross-validation for trending topics.
**Subreddits to monitor:** Configure in your `my-niche/sources.md` based on your niche.

---

## Optional MCPs (Depending on Your Niche)

### GitHub Trending
**Best for:** Developer, open source, tools niches
**What it does:** Shows which repos are trending by language and timeframe.
**Tools:** `get_github_trending_repositories`

### RSS Aggregator
**Best for:** News-heavy niches, industry monitoring
**What it does:** Fetches articles from configured RSS feeds.
**Setup:** Configure your feeds in the MCP settings.

### Exa (Semantic Search)
**Best for:** Finding content by description rather than keywords.
**What it does:** Semantic/meaning-based web search. Great for discovering pages like "blog post comparing React and Vue for beginners."
**Tools:** `web_search_exa`, `web_fetch_exa`
**Setup:** Free tier available at [exa.ai](https://exa.ai). Add to your global MCP config.

### HackerNews
**Best for:** Tech, startup, developer, AI niches
**What it does:** Checks front page stories, searches by topic, monitors community sentiment.
**Tools:** `get_stories`, `search_stories`, `get_story_info`
**Setup:** `mcp-hn` — standalone binary, no API key needed.

### Apify (Web Browser)
**Best for:** Deep research, scraping specific URLs for full article content.
**What it does:** Fetches and reads full web pages via a real browser, extracts content as markdown.
**Tools:** `rag-web-browser`
**Setup:** Requires an Apify account and API token.

---

## Do I Need MCPs?

| Your content style | MCPs needed |
|-------------------|-------------|
| News/commentary (reactive to current events) | Built-in web search + Reddit minimum |
| Evergreen content (tips, tutorials, stories) | Built-in web search is sufficient |
| Memes/humor about your industry | Reddit for community pulse |
| Personal stories/life content | No MCPs needed |

---

## How to Set Up MCPs

Setup depends on your AI tool:

**Kiro:** MCPs are configured in `.kiro/settings/mcp.json` (workspace) or `~/.kiro/settings/mcp.json` (global).

**Claude Code:** MCPs are configured in `.mcp.json` in your project root or `~/.claude/settings/mcp.json` globally.

**Cursor:** MCP support varies. Check Cursor documentation for current setup.

---

## Using MCPs Without the News Scout Module

Even without the news-scout module active, MCPs help with:
- Researching a specific topic the user asks about
- Fact-checking claims before posting
- Finding data points and statistics
- Getting current context for any post topic

The news-scout module just adds a structured scouting workflow on top of the raw MCP tools.
