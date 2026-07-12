# Manual Setup

If you prefer to configure your pipeline yourself instead of using guided setup.

---

## What You Need to Create

Create these files in the `my-niche/` folder:

### Required Files

**1. `niche.yaml`** — Your identity and configuration

```yaml
name: Your Niche Name
identity:
  description: Who you are and what you do
  personality: How you come across (e.g., professional, casual, funny)
  expertise:
    - Topic 1
    - Topic 2
    - Topic 3

platforms:
  - linkedin  # default, add more as needed

content_pillars:
  - name: "Main Topic"
    percentage: 50
  - name: "Secondary Topic"
    percentage: 30
  - name: "Personal/Other"
    percentage: 20

cadence:
  max_per_day: 2
  best_days:
    - tuesday
    - wednesday
    - thursday
    - friday
  timezone: "America/New_York"  # your timezone

sources:
  subreddits:
    - your_niche_subreddit
    - another_relevant_sub
  hackernews: false  # true if tech-relevant
  github_trending: false  # true if dev-relevant

modules_active:
  - visual-system  # remove if you don't use images
  # - memes         # uncomment if you do humor
  # - news-scout    # uncomment if you post about news
```

**2. `voice.md`** — How you sound

Write in plain language how you want your posts to sound. Include:
- What tone you use (casual, professional, aggressive, warm)
- Words/phrases you naturally use
- What you NEVER want to sound like
- How your voice changes for different content types

Look at `examples/ai-tech/voice.md` for a detailed reference.

**3. `content-rules.md`** — What and how you post

Define:
- Length guidelines per post type
- Post structure (hook, body, CTA)
- Hook styles you prefer
- Any rules specific to your niche (e.g., "never promote without disclosing")

Look at `examples/ai-tech/content-rules.md` for reference.

---

### Optional Files

**4. `sources.md`** — Where you find content ideas (needed if news-scout active)

**5. `hashtags.yaml`** — Your hashtag strategy

```yaml
always:
  - "#yourniche"
  - "#maintopic"

topics:
  subtopic1:
    - "#related1"
    - "#related2"
  subtopic2:
    - "#related3"
    - "#related4"
```

**6. Module files** — Copy from `engine/modules/` and customize:
- `visual-system.md` — if you use images
- `memes.md` — if you do humor
- `news-scout.md` — if you post about trending topics
- `video-content.md` — if you create video
- `image-prompts.md` — if you use AI-generated images
- `analytics.md` — if you want performance tracking
- `repurpose.md` — if you post to multiple platforms
- `carousel.md` — if you do carousel/slide content

---

## Validation

After creating your files, tell the AI: "let's go" or "write a test post about [topic]"

If anything is missing or unclear, the AI will tell you what needs fixing.

---

## Tips

- Start minimal: just `niche.yaml`, `voice.md`, and `content-rules.md`
- Add modules later as you need them
- Look at `examples/ai-tech/` for a complete working reference
- Everything is editable anytime — nothing is locked in
