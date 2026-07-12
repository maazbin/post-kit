# Web Research

Boosts any agent's built-in web search into structured, multi-source research. This is the engine that powers the Research step in the pipeline.

Works with any agent runtime's search tools — no external MCPs or API keys required.

---

## When to Use

- Pipeline Step 1 (Research) — always route through this
- User asks to research a topic for content
- Fact-checking claims before posting
- Finding data, stats, or sources for any post
- Discovering what's current on a topic
- Content research mode: finding what happened, why it matters, what the take is

---

## Phase 1: Classify Intent

Before searching, determine what kind of research this is:

| Intent | Signals | Depth |
|--------|---------|-------|
| **Quick fact** | "what is", "when", specific data point | 1-2 searches, snippets may suffice |
| **Topic research** | "what's happening with", general topic exploration | 3 searches, fetch 1-2 pages |
| **Content sourcing** | Need a topic for a post, need angles and data | 3-4 searches, fetch 2-3 pages |
| **Deep investigation** | "research", "deep dive", compare options | 4-6 searches, fetch 3-5 pages |
| **Trend scouting** | "what's trending", "latest news on" | 3 searches with freshness filters |

---

## Phase 2: Multi-Angle Search

Never search once. Always search from multiple angles.

### Core Pattern (minimum for any research)

| Angle | Query Template | Purpose |
|-------|---------------|---------|
| **Direct** | User's question rewritten as search keywords | Primary results |
| **Community** | Query + "reddit" OR "developers say" OR "discussion" | Real opinions, sentiment |
| **Authoritative** | Query + "official" OR "documentation" OR site-specific | Primary sources |

### Additional Angles (add based on intent)

| Angle | When to Use | Template |
|-------|-------------|----------|
| **Recency** | Tech, news, fast-moving topics | Query + current year |
| **Contrarian** | Comparisons, decisions | Query + "problems" OR "criticism" |
| **Data** | Need stats for content | Query + "statistics" OR "benchmark" OR "report" |
| **Reaction** | Content about announcements | Query + "reaction" OR "response" OR "opinion" |

### Query Crafting Rules

1. **Be specific** — include versions, years, context
2. **Describe the ideal page** — natural language works better than keyword soup
3. **Vary your keywords** — don't use the same words across all angles
4. **Use site operators** when you know where good content lives
5. **Break compound questions** into independent sub-queries

### Parallel Execution

Run all search angles in parallel when possible. Sequential only if forced.

---

## Phase 3: Source Triage

After searches return, score results before committing to full fetches:

### Triage Scoring

| Signal | Priority |
|--------|----------|
| Appears in 2+ search angles | Highest — cross-validated |
| Official or primary source | High |
| Published in last 6 months | High for tech/news |
| Contains specific data/numbers | Medium-High |
| From reputable domain | Medium |
| Single appearance, blog quality | Low |

### Fetch Budget

| Research depth | Full pages to fetch |
|---------------|-------------------|
| Quick fact | 0-1 |
| Topic research | 1-2 |
| Content sourcing | 2-3 |
| Deep investigation | 3-5 |

### Discard & Retry

If results are weak, off-topic, or outdated:
- Do NOT use them anyway
- Reformulate with different keywords
- Try a completely different angle
- If still poor → be honest about it

---

## Phase 4: Extract & Verify

When reading full pages:

1. **Pull key passages** — the 2-4 most relevant paragraphs, not the whole page
2. **Cross-reference** — single-source claims get flagged
3. **Check dates** — stale info on fast-moving topics gets noted
4. **Surface conflicts** — if sources disagree, present both sides
5. **Separate fact from opinion** — community sentiment ≠ verified data

---

## Phase 5: Synthesize for Content

For content research specifically, organize findings into:

```
WHAT HAPPENED → WHY IT MATTERS → THE ANGLE/TAKE
```

Deliver to the pipeline:
- **The hook** — the most interesting or surprising finding
- **The data** — specific numbers, quotes, or facts that make the post credible
- **The sources** — links for attribution and credibility
- **The angle** — what makes this interesting for the user's audience
- **Conflicting views** — if relevant, what's the debate?

---

## Quality Rules

1. **Every factual claim needs a source.** No exceptions.
2. **Cross-reference.** Single-source claims are flagged as unverified.
3. **Recency matters.** Prefer last 6-12 months for tech/news.
4. **Acknowledge gaps.** "Couldn't find reliable info on X" is valid.
5. **No hallucinated URLs.** Only cite pages actually found in search results.
6. **Snippets ≠ evidence.** Substantive claims need full-page verification.
7. **Discard and retry** over serving weak results.

---

## Source Priority

When multiple sources exist, prefer:

1. Official documentation, announcements, primary sources
2. Peer-reviewed studies, established technical blogs
3. Community discussions with specific experience (Stack Overflow, GitHub issues)
4. Reddit/forums (good for sentiment, unreliable for facts)
5. General blog posts (verify independently)

---

## Integration with Pipeline

This module powers **Step 1: Research** in `pipeline.md`.

When the pipeline's research step fires:
1. Route through this module
2. Use the appropriate depth based on what the user asked
3. Present findings in the content-ready format (what/why/angle)
4. Let the user pick direction before moving to Step 2: Write

When fact-checking during writing:
1. Use the quick-fact depth
2. Verify specific claims the post makes
3. Add sources to strengthen the post's credibility
