# post-kit

A content pipeline that works for any niche. Set up your voice. Start posting.

No code. No subscriptions. Just markdown files your AI tool reads and follows.

---

## What is this?

post-kit is a content creation framework powered by your AI coding assistant. You configure your niche, voice, and style — the AI handles research, writing, voice matching, and quality control for every post.

It works for any niche: AI/tech, fitness, crypto, real estate, cooking, fashion, marketing — anything.

## What you get

- A voice that sounds like YOU, not AI
- Research-backed posts from real trending sources
- Platform-optimized content (LinkedIn default, X, YouTube, more)
- Anti-AI pass on every post (removes robotic language automatically)
- Modular — only use what you need (visuals, memes, news scouting, video)
- Brainstorm skill — improve any part of your pipeline through conversation

## Install

Pick your tool:

### Kiro (one click)
1. Go to kiro.dev/powers or open Powers panel in Kiro
2. Search "post-kit"
3. Click Install

### Claude Code (one command)
```
/plugin install post-kit@claude-plugins-official
```
Or from GitHub:
```
claude plugin install github:yourname/post-kit
```

### Cursor
Settings → Rules/Skills → Add from GitHub → paste:
```
https://github.com/yourname/post-kit
```

### Any other AI tool
Clone this repo and open the folder in your tool:
```
git clone https://github.com/yourname/post-kit
```

## Quick Start

After install, start a conversation with your AI tool. It will greet you:

> "Welcome to post-kit! Would you like guided setup or manual?"

Pick **guided** — answer a few questions about your niche, voice, and style. The AI builds your entire pipeline from your answers. You're posting in 5 minutes.

## How it works

```
Research → Write → Voice Pass → Anti-AI Pass → Quality Gate → Post
```

Every post goes through this pipeline. The AI researches your topic, writes a draft, matches your voice, removes AI-sounding language, checks quality, and delivers a ready-to-post output.

## Modules (use what you need)

| Module | What it does |
|--------|-------------|
| Visual system | Image approach for your posts |
| Memes | Humor, roasts, meme pipeline |
| News scout | Trending topic discovery |
| Video content | Short-form video creation |
| Image prompts | AI image generation |
| Analytics | Track what works, improve over time |
| Repurpose | Turn 1 post into multi-platform content |
| Carousel | Slide/carousel creation |

Modules are optional. If you don't need memes, don't enable it. Want to add video later? Just say "I want to do video" and the AI sets it up.

## Platforms

LinkedIn is the default. You can add or switch to:
- X (Twitter)
- YouTube Community
- Newsletter
- Blog

Add platforms during setup or anytime after.

## Change anything, anytime

- Change your niche → edit your config files or tell the AI
- Add a module → tell the AI or drop a .md file in your config
- Remove a module → delete the file
- Switch platforms → update your config
- Improve your pipeline → use the brainstorm skill

## MCP Tools (for research)

post-kit works best with these MCP tools connected:

**Universal (recommended for everyone):**
- Web search
- Reddit

**Optional (depending on your niche):**
- HackerNews — tech/startup niches
- GitHub Trending — developer niches
- RSS feeds — news-heavy niches
- Apify — deep research

See [docs/mcps.md](docs/mcps.md) for setup instructions.

## Example

The `examples/ai-tech/` folder contains a complete, proven niche pack for AI/tech content creation. Study it to understand how everything connects, or use it as a starting template.

## Contributing

We welcome contributions:
- New niche packs (share your config for others in your niche)
- New modules (new capabilities anyone can use)
- New platform files (research + document a new platform)
- Improvements to existing files

See [docs/contributing.md](docs/contributing.md) for guidelines.

## License

MIT — use it however you want.
