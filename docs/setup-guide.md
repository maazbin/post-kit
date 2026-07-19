# Setup Guide

This is the manual setup path. If you prefer the AI to walk you through it conversationally, just open a chat and pick "Guided" when asked.

---

## What You're Building

A `my-niche/` folder with files that define YOUR content pipeline. The AI reads these files every time you ask it to create a post. More files = more capabilities. Fewer files = simpler pipeline.

---

## Minimum Setup (3 files)

You need at least these 3 files to start:

### 1. `my-niche/niche.yaml`

Your identity and basic config. Copy this template and fill it in:

```yaml
postkit_version: "1.0.0"  # don't change manually — used by the update system

name: [Your niche — e.g., "Fitness Coaching", "Web3", "SaaS Marketing"]

identity:
  description: [One sentence about who you are and what you do]
  personality: [How you come across — e.g., "Direct, practical, no fluff"]
  expertise:
    - [Topic 1]
    - [Topic 2]
    - [Topic 3]

platforms:
  - linkedin   # default. Add: x, youtube-community, newsletter, blog

content_pillars:
  - name: "[Your main topic]"
    percentage: [number]
  - name: "[Second topic]"
    percentage: [number]
  - name: "[Third topic]"
    percentage: [number]
  # Percentages should add up to 100

cadence:
  max_per_day: 2
  best_days: [monday, tuesday, wednesday, thursday, friday]  # pick your best
  timezone: "[Your/Timezone]"  # e.g., America/New_York, Europe/London

sources:
  subreddits:
    - [relevant_subreddit_1]
    - [relevant_subreddit_2]
  hackernews: false  # true if your niche is tech-related
  github_trending: false  # true if your audience is developers
```

### 2. `my-niche/voice.md`

How you sound. Write this in plain language. Include:

```markdown
# Voice

## Sound Like
[Describe how you want to come across. Think: if a friend described your posting style, what would they say?]

## Rules
- [Rule 1 — e.g., "Always use first person"]
- [Rule 2 — e.g., "Short sentences, max 2 lines per paragraph"]
- [Rule 3 — e.g., "State opinions directly, never hedge"]
- [Rule 4 — e.g., "Warm on personal stuff, sharp on industry stuff"]

## Never Sound Like
- [What you don't want — e.g., "Corporate press release"]
- [Another thing — e.g., "Motivational speaker"]
- [Another thing — e.g., "Generic AI output"]
```

### 3. `my-niche/content-rules.md`

What you post and how. Define your structure:

```markdown
# Content Rules

## Length
| Type | Length |
|------|--------|
| [Your post type 1] | [e.g., 50-100 words] |
| [Your post type 2] | [e.g., 1-4 lines] |
| [Your post type 3] | [e.g., 100-200 words] |

## Structure
[Hook — 1-2 lines]
[Body]
[CTA — what you want readers to do]

## Hooks
[Describe your hook style. How do your posts open?]

## Rules
- [Any content rules specific to your niche]
- [e.g., "Always include one data point"]
- [e.g., "Never promote without disclosing"]
```

---

## That's It For Minimum

With just those 3 files, you can start creating content. Tell the AI "write a post about [topic]" and it'll use your config.

---

## Optional: Add More

### Hashtags (`my-niche/hashtags.yaml`)

```yaml
always:
  - "#yourniche"
  - "#maintopic"

topics:
  subtopic1:
    - "#tag1"
    - "#tag2"
  subtopic2:
    - "#tag3"
    - "#tag4"
```

### Sources (`my-niche/sources.md`)

Where you find content ideas. Useful if you enable the news-scout module.

### Modules

Copy any of these from `engine/modules/` into `my-niche/` and customize:

| Module | Copy if you... |
|--------|---------------|
| `visual-system.md` | Post images with your content |
| `memes.md` | Do humor, roasts, or memes |
| `news-scout.md` | Post about trending topics/news |
| `video-content.md` | Create short-form video |
| `image-prompts.md` | Use AI-generated images |
| `analytics.md` | Want data-driven improvements |
| `repurpose.md` | Post to multiple platforms |
| `carousel.md` | Create slide/carousel content |

---

## Reference

Look at `examples/ai-tech/` for a complete working setup. It shows every file filled in with real content.

---

## Test Your Setup

After creating your files, tell the AI:

> "Write a test post about [any topic in your niche]"

If everything is configured correctly, you'll get a post that matches your voice, follows your rules, and passes through the anti-AI filter. If something's off, the AI will tell you what's missing.
