# Modules

Modules are optional capabilities you can add to your pipeline. Each module is a single `.md` file. If the file exists in your `my-niche/` folder, it's active. If it doesn't exist, it's invisible.

---

## Core Engine (always active)

These live in `engine/core/` and power every post automatically. You don't enable or disable them — they're always on.

| File | What it does |
|------|-------------|
| `pipeline.md` | The master flow: Research → Write → Voice → Anti-AI → Quality Gate → Output |
| `web-research.md` | **Search amplifier.** Turns any agent's basic web search into multi-angle research with intent classification, query decomposition, source triage, cross-validation, and citation. No MCPs or API keys needed. |
| `anti-ai-writing.md` | Strips AI-sounding language from every post. Mandatory, cannot be disabled. |
| `quality-gates.md` | Every post must pass all gates before output. |
| `onboarding.md` | First-time guided setup flow. |
| `brainstorm.md` | Collaborative improvement skill for any part of the pipeline. |

---

## Optional Modules

## How to Enable an Optional Module

**Option A (guided):** Tell the AI "I want to start doing [memes/video/etc]" → it asks you setup questions and creates the file.

**Option B (manual):** Copy the template from `engine/modules/[module-name].md` into your `my-niche/` folder and customize it.

## How to Disable an Optional Module

Delete the file from `my-niche/`. Or tell the AI "I don't want [module] anymore."

---

## Available Modules

### visual-system.md
**What it does:** Decides how to handle images/visuals for every post. Recommends screenshots, stock photos, text cards, or AI-generated images based on post content.

**Good for:** Anyone who posts images alongside their text content.

**Key features:**
- Visual selection priority (real screenshots first, AI last)
- Post-type to visual-type mapping
- Image specs per platform
- Tells you when to skip images entirely

---

### memes.md
**What it does:** Handles humor, roasts, memes, and comedy-driven content.

**Good for:** Creators whose personality includes humor, roasting, or commentary with an edge.

**Key features:**
- Meme format library (screenshot + caption, fake Slack, parody terminal, etc.)
- Roast calibration levels (light/medium/spicy)
- Timeliness rules (post within hours or skip)
- Targets to roast vs never roast

---

### news-scout.md
**What it does:** Discovers trending topics in your niche by checking multiple sources and cross-validating.

**Good for:** Creators who post about current events, news, or react to what's happening in their industry.

**Key features:**
- Multi-source scouting (Reddit, HackerNews, RSS, GitHub)
- Cross-validation rule (2+ sources = candidate)
- Urgency scoring (post now vs queue)
- Anti-bias checks

---

### video-content.md
**What it does:** Handles short-form video creation specs, scripts, and storyboards.

**Good for:** Creators making Reels, TikToks, Shorts, or any video content.

**Key features:**
- Specs per platform (duration, format, size)
- Video type templates (meme clips, text-on-video, demos, talking head)
- Quality rules (works without sound, readable text, 2-second hook)
- Text overlay guidelines

---

### image-prompts.md
**What it does:** Generates multiple AI image prompts when no real image fits the post.

**Good for:** Creators who use AI image generation tools (Midjourney, DALL-E, etc.)

**Key features:**
- 4-prompt system exploring different visual angles
- Angle categories per content type (pricing, launches, drama, humor, opinion)
- Prompt formula (subject + setting + style + lighting + camera + mood)
- Only used as last resort when real images aren't available

---

### analytics.md
**What it does:** Tracks what's working in your content strategy and feeds insights back into the pipeline.

**Good for:** Anyone who wants data-informed content decisions.

**Key features:**
- Performance tracking template (by topic, format, post)
- Learning loop (past data informs future topic/format selection)
- Anti-bias warnings (don't over-optimize for what worked before)
- Growth targets

---

### repurpose.md
**What it does:** Adapts one piece of content for multiple platforms.

**Good for:** Multi-platform creators who don't want to write from scratch for each platform.

**Key features:**
- Platform-to-platform adaptation rules
- What changes for each platform (not just reformatting)
- What's repurposable vs what's not
- Separate output per platform

---

### carousel.md
**What it does:** Handles multi-slide/carousel content creation.

**Good for:** LinkedIn or Instagram creators who make slide-based content.

**Key features:**
- Carousel structure (cover → body slides → closing CTA)
- Slide specs per platform
- Design principles (one idea per slide, readable on mobile)
- Text rules (word limits, font sizes)

---

## Creating Custom Modules

You can create any module you want. Just write a `.md` file explaining what the AI should do, and drop it in your `my-niche/` folder. The AI reads whatever files exist and follows them.

Examples of custom modules you might create:
- `ebook-promotion.md` — rules for promoting your ebook
- `collaboration.md` — how to approach and post about collabs
- `seasonal.md` — seasonal content calendar
- `ugc-repost.md` — rules for reposting user-generated content
