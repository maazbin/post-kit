# Pipeline

The universal content creation flow. Every post goes through these steps in order.

---

## Flow

```
Request → Research → Write → Voice Pass → Anti-AI Pass → Quality Gate → Output
```

---

## Step 1: Research

**Skip if:** the user provides a specific topic with enough context, or news-scout module is not active.

**Run if:** user says "what's trending", "find me something to post about", or the topic needs current data.

**If the user asks "what's trending" / "find me topics" / "what should I post about":** run **The Daily Scout Command** defined in `my-niche/news-scout.md` — follow the candidate composition and presentation rules defined there, then let the user pick which to write.

**How to research — follow `engine/core/web-research.md`:**

The web-research module handles all search strategy. It will:
1. Classify the research intent (quick fact vs deep investigation)
2. Run multi-angle searches (direct + community + authoritative)
3. Triage sources by quality, recency, and cross-validation
4. Fetch and extract key passages from top sources
5. Synthesize findings into content-ready format (what happened → why it matters → the angle)

**Additional source checks:**
- Check the user's `sources.md` for where to look (subreddits, feeds, communities)
- Cross-validate: a topic is worth posting about if it appears in 2+ independent sources
- Score urgency:
   - Happening right now → post today
   - Trending this week → post within 2-3 days
   - Evergreen → queue for whenever

Present research findings to the user. Let them pick or direct you.

---

## Step 2: Write

Read these files before drafting:
- `my-niche/niche.yaml` — their identity and content pillars
- `my-niche/content-rules.md` — post structure, length, hooks
- Active platform file from `engine/platforms/` — format constraints

Then draft the post following the structure defined in their content-rules.

### Writing principles:
- One idea per post
- Hook in the first 1-2 lines (the "see more" gate on most platforms)
- Short sentences, short paragraphs
- Include one genuine personal opinion
- End with a CTA that invites disagreement or experience-sharing
- Match the length rules from content-rules.md

---

## Step 3: Voice Pass

Read `my-niche/voice.md` and rewrite the draft to match their voice profile.

Check:
- Does this sound like THEM, not generic AI?
- Are the voice rules being followed? (tone, banned phrases, personality)
- Would they actually say this out loud?

If it doesn't pass, rewrite until it does.

---

## Step 4: Anti-AI Pass (Mandatory)

Read `engine/core/anti-ai-writing.md` and run the full check.

This step is ALWAYS active. It cannot be disabled. Every post must pass.

- Remove banned words
- Remove banned patterns
- Check for AI-sounding structure
- Make it sound human

---

## Step 5: Quality Gate

Read `engine/core/quality-gates.md` and evaluate the post.

The post must pass ALL gates to be published. If it fails any gate, revise and re-run from Step 3.

---

## Step 6: Output

1. Create the output folder: `posts/YYYY-month/YYYY-MM-DD-slug/`
   - **No subfolders** inside the month folder (no `daily/`, `news/`, `github/`)
   - Every post goes flat inside the month, identified by its date-slug folder
   - Example: `posts/2026-july/2026-07-14-slug/linkedin-post.md`
2. Save the post as `linkedin-post.md` (or `x-post.md` if platform-specific)
3. If image-prompts module is active, include 3 AI image prompts in the post file
4. If github-screenshot module is active and this is a repo post, capture/provide screenshot
5. Present the final post to the user for approval

---

## Dedup Check

Before writing, check existing posts in `posts/` for the current month. If a post with a similar slug or topic already exists, inform the user and ask if they want to proceed or pick a different angle.

---

## Platform Adaptation

If the user has multiple platforms active, ask:
> "Want me to write this for LinkedIn only, or adapt it for [other active platforms] too?"

If adapting for multiple platforms, run Steps 2-5 once per platform, following each platform's specific rules from `engine/platforms/`.
