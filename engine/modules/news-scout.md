# News Scout Module

Handles trending topic discovery, cross-validation, and urgency scoring. Activate this if your content is news-based or reactive to what's happening in your space.

---

## Core Rule

Trending = 2+ independent sources + velocity (engagement/time). One source alone is not enough. Cross-validate before posting.

---

## Scouting Flow

```
1. Check sources from my-niche/sources.md
2. Identify topics appearing in 2+ sources
3. Score urgency
4. Present candidates to user
5. Deep research on selected topic
6. Hand off to pipeline for writing
```

---

## Source Layers

Configure these in `my-niche/sources.md` based on your niche:

| Layer | Purpose | Examples |
|-------|---------|----------|
| L1: Real-time signals | What's happening NOW | Reddit hot posts, HackerNews front page, X trending |
| L2: Research/depth | What's being published | Academic papers, long-form articles, reports |
| L3: Builder signals | What's being created | GitHub trending, Product Hunt, new tools |
| L4: Context/press | What's being reported | Industry news sites, newsletters, press |

Not every niche needs all layers. A fitness creator might only use L1 (Reddit) and L4 (health news sites).

---

## Cross-Validation Rule

A topic is a candidate for posting when:
- It appears in 2+ independent sources from different layers
- OR it has extreme velocity in a single source (top of HN, viral Reddit post)
- AND it's relevant to your niche/pillars

If only one source mentions it and it's not viral, skip it or queue for later.

---

## Urgency Scoring

| Urgency | Signal | Action |
|---------|--------|--------|
| Immediate (0.7-1.0) | Breaking news, just announced, going viral | Post today |
| High (0.4-0.7) | Trending topic, multiple sources, growing | Post within 1-2 days |
| Medium (0.15-0.4) | Interesting but not urgent | Queue for slow days |
| Low (<0.15) | Old news or declining interest | Skip |

---

## Scouting with MCP Tools

If MCP tools are available, use them:

**Web search:** Search for recent developments in the user's niche topics.

**Reddit:** Check the subreddits listed in sources.md for:
- Hot posts (what's popular right now)
- Rising posts (what's gaining momentum)

**HackerNews (if available):** Check front page and search for niche keywords.

**GitHub Trending (if available):** Check trending repos related to the niche.

**RSS (if available):** Scan configured feeds for multi-source stories.

---

## Presenting Candidates

After scouting, present findings to the user:

```
Here's what I found trending in [niche] today:

1. [Topic] — [urgency] — appeared in [sources]
   Why it matters: [one line]

2. [Topic] — [urgency] — appeared in [sources]
   Why it matters: [one line]

3. [Topic] — [urgency] — appeared in [sources]
   Why it matters: [one line]

Which one do you want to post about? Or should I look for something else?
```

---

## Deep Research

Once the user picks a topic:
1. Use web search to get full context (original source, official announcements)
2. Get multiple perspectives (how different communities are reacting)
3. Find specific data points (numbers, dates, names, quotes)
4. Check what angle hasn't been covered yet (your unique take)

Hand all research to the pipeline for writing.

---

## Anti-Bias Rules

Before posting, check:
1. Appears in 2+ independent sources?
2. Is this actual impact (data, users, real change) or just an announcement?
3. Am I covering this because it's important, or because it's from a popular/familiar source?
4. Who did similar work and got zero coverage?

---

## Scouting Schedule (Suggested)

- Morning: Full scout across all sources
- Afternoon: Quick check for anything that broke since morning
- If nothing's trending: skip, post evergreen content instead

Never force a news post when nothing meaningful is happening.
