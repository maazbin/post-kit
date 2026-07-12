# MCP Tools

MCP (Model Context Protocol) tools give your AI agent the ability to research topics in real time — searching the web, checking Reddit, monitoring HackerNews, and more.

---

## What Are MCPs?

MCPs are plugins that connect your AI tool to external services. They let the AI actually search the internet, check Reddit, and pull live data instead of relying on its training knowledge.

Without MCPs, the AI can still write posts but can't research what's currently trending.

---

## Universal MCPs (Recommended for Everyone)

These work for any niche:

### Web Search
**What it does:** Searches the internet for current information on any topic.
**Why you need it:** Research, fact-checking, finding context for trending topics.
**Setup:** Usually built into your AI tool (Kiro, Claude Code). No extra setup needed.

### Reddit
**What it does:** Checks subreddit posts (hot, rising, top) for what your audience is talking about.
**Why you need it:** Real-time pulse on your community. Cross-validation for trending topics.
**Subreddits to monitor:** Configure in your `my-niche/sources.md` based on your niche.

---

## Optional MCPs (Depending on Your Niche)

### HackerNews
**Best for:** Tech, startup, developer, AI niches
**What it does:** Checks front page stories, searches by topic, monitors community sentiment.
**Tools:** `get_stories`, `search_stories`, `get_story_info`

### GitHub Trending
**Best for:** Developer, open source, tools niches
**What it does:** Shows which repos are trending by language and timeframe.
**Tools:** `get_github_trending_repositories`

### RSS Aggregator
**Best for:** News-heavy niches, industry monitoring
**What it does:** Fetches articles from configured RSS feeds.
**Setup:** Configure your feeds in the MCP settings.

### Apify (Web Browser)
**Best for:** Deep research, scraping specific URLs for full article content.
**What it does:** Fetches and reads full web pages, extracts content.
**Tools:** `rag-web-browser`

---

## Do I Need MCPs?

| Your content style | MCPs needed |
|-------------------|-------------|
| News/commentary (reactive to current events) | Yes — web search + Reddit minimum |
| Evergreen content (tips, tutorials, stories) | Optional — web search is helpful but not required |
| Memes/humor about your industry | Yes — Reddit for community pulse |
| Personal stories/life content | No MCPs needed |

---

## How to Set Up MCPs

Setup depends on your AI tool:

**Kiro:** MCPs are configured in `~/.kiro/settings/mcp.json`. Some powers include MCP configs automatically.

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
