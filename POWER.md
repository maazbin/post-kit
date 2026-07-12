---
name: "post-kit"
displayName: "post-kit — Content Pipeline for Any Niche"
description: "Zero-code content creation pipeline. Research, write, and polish posts that sound like you — for any niche, any platform. Guided setup, modular features, anti-AI writing built in."
keywords: ["content", "post", "write a post", "linkedin", "twitter", "social media", "content creation", "trending", "news", "meme", "roast", "write", "draft", "publish", "what's trending", "improve my voice", "brainstorm", "content pipeline", "hashtags"]
author: "post-kit"
---

# post-kit

A content pipeline that works for any niche. Powered by your AI coding assistant.

## Onboarding

### Step 1: Check if setup is complete

Check if `my-niche/niche.yaml` exists in the user's workspace.

- If it exists → skip onboarding, go to Steering Instructions
- If it doesn't exist → run the onboarding flow from `engine/core/onboarding.md`

### Step 2: Run onboarding (first time only)

Follow the instructions in `engine/core/onboarding.md` exactly. Ask the user if they want guided or manual setup, then proceed accordingly.

## Steering Instructions

### Core Pipeline

Every content request goes through the pipeline defined in `engine/core/pipeline.md`:

```
Research → Write → Voice Pass → Anti-AI Pass → Quality Gate → Output
```

Always read these files before producing any content:
- `my-niche/niche.yaml` — user's identity and content pillars
- `my-niche/voice.md` — how they sound
- `my-niche/content-rules.md` — post structure, length, hooks
- `engine/core/anti-ai-writing.md` — mandatory humanizer pass
- `engine/core/quality-gates.md` — every post must pass all gates

### Research Engine

All web research goes through `engine/core/web-research.md`. This includes:
- Topic research for posts
- Fact-checking claims
- Finding sources, stats, and data
- Trend discovery and validation

Read this file whenever the pipeline's research step fires, or when any task needs web search.

### Platform Rules

Read the relevant platform file based on what the user has configured:
- LinkedIn → `engine/platforms/linkedin.md`
- X (Twitter) → `engine/platforms/x.md`
- YouTube → `engine/platforms/youtube-community.md`
- Newsletter → `engine/platforms/newsletter.md`
- Blog → `engine/platforms/blog.md`

### Active Modules

Check `my-niche/` for any of these files. If they exist, follow their instructions when relevant:
- `visual-system.md` → handle visuals for posts
- `memes.md` → humor/roast pipeline
- `news-scout.md` → trending topic discovery
- `video-content.md` → video creation
- `image-prompts.md` → AI image generation
- `analytics.md` → performance-informed decisions
- `repurpose.md` → multi-platform adaptation
- `carousel.md` → carousel/slide content

### Brainstorm Skill

When the user asks to improve any part of their pipeline, follow `engine/core/brainstorm.md`.

### Output

Save posts to: `posts/YYYY-month/YYYY-MM-DD-slug/post.md`

The output folder structure can be customized by the user.
