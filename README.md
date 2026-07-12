<div align="center">

# post-kit

**Your AI assistant's content engine.** Research, write, and publish posts that sound like you — zero code, any niche, any platform.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Works with Kiro](https://img.shields.io/badge/Works_with-Kiro-blue.svg)](https://kiro.dev)
[![Works with Claude Code](https://img.shields.io/badge/Works_with-Claude_Code-orange.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Works with Cursor](https://img.shields.io/badge/Works_with-Cursor-purple.svg)](https://cursor.com)

[Quick Start](#-quick-start) · [How It Works](#-how-it-works) · [Modules](#-modules) · [Examples](#-examples) · [Contributing](#-contributing)

</div>

---

## What Comes Out

I said _"write a post about RAG chunking strategies"_ — here's what the pipeline produced in 90 seconds:

> Most teams tune their embedding model obsessively and ignore how they split their documents. That's backwards.
>
> A Vectara study published at NAACL 2025 tested 25 chunking configurations with 48 embedding models. The finding: chunking configuration had as much or more influence on retrieval quality as the choice of embedding model.
>
> The practical defaults from four independent benchmarks:
>
> → Start with recursive splitting at 512 tokens, 50-100 token overlap
> → Factoid queries: 256-512 tokens work fine
> → Analytical/multi-hop queries: bump to 512-1,024 tokens
>
> What chunking strategy are you running in production?

No "delve." No "it's worth noting." No "in today's rapidly evolving landscape." Just a real person with real opinions sharing something useful.

---

## 🚫 The Anti-AI Pass (Before → After)

<table>
<tr>
<th>❌ Before (raw AI output)</th>
<th>✅ After (anti-AI pass)</th>
</tr>
<tr>
<td>

It's worth noting that in today's rapidly evolving AI landscape, leveraging robust chunking strategies is crucial for building comprehensive RAG pipelines. Furthermore, this groundbreaking approach empowers developers to streamline their retrieval systems seamlessly.

</td>
<td>

Most teams tune their embedding model obsessively and ignore how they split their documents. That's backwards. Chunking configuration had as much or more influence on retrieval quality as the choice of embedding model.

</td>
</tr>
</table>

The anti-AI pass runs on **every** post. It catches 50+ banned words, AI sentence patterns, hedging language, and robotic structure — then rewrites until it sounds like a human wrote it.

---

## ✨ Features

| Feature | What it does |
|---------|-------------|
| 🎙️ **Voice matching** | Learns how you sound — posts read like YOU wrote them |
| 🚫 **Anti-AI filter** | Automatically removes robotic language, every post, no exceptions |
| 🔬 **Research-backed** | Pulls from Reddit, HackerNews, RSS, web — cross-validates sources |
| 📦 **Modular** | Only enable what you need (visuals, memes, news, video, analytics) |
| 📱 **Multi-platform** | LinkedIn, X, YouTube, Newsletter — one post adapts to many |
| ⚡ **5-minute setup** | Guided onboarding — answer 10 questions, start posting immediately |

---

## 🚀 Quick Start

### 1. Install

<details>
<summary><b>Kiro</b> (recommended)</summary>

Go to Powers panel → search "post-kit" → click Install

</details>

<details>
<summary><b>Claude Code</b></summary>

```
claude plugin install github:Huzaifa-ali/post-kit
```

</details>

<details>
<summary><b>Cursor</b></summary>

Settings → Rules/Skills → Add from GitHub → paste the repo URL

</details>

<details>
<summary><b>Any other AI tool</b></summary>

```bash
git clone https://github.com/Huzaifa-ali/post-kit
```

Open the folder in your tool. The AI reads the markdown files automatically.

</details>

### 2. Set up your pipeline

Start a conversation. The AI will ask:

> "Welcome to post-kit! Guided or manual setup?"

Pick **guided** — answer 10 questions about your niche, voice, and style. Takes 3 minutes.

### 3. Start posting

```
"Write a post about [topic]"
```

That's it. The pipeline handles research, writing, voice matching, anti-AI filtering, and quality checks.

---

## ⚙️ How It Works

<p align="center">
  <img src="docs/images/pipeline-flow.svg" alt="post-kit pipeline: Research → Write → Voice Pass → Anti-AI → Quality Gate → Publish" width="800"/>
</p>

Every post goes through this pipeline automatically:

1. **Research** — Finds trending topics from your configured sources (Reddit, HN, RSS)
2. **Write** — Drafts following your content rules (length, structure, hooks)
3. **Voice Pass** — Rewrites to match YOUR voice profile
4. **Anti-AI Pass** — Strips banned words, AI patterns, robotic structure _(mandatory, always on)_
5. **Quality Gate** — Checks hook strength, one-idea rule, save/share test, platform compliance
6. **Output** — Saves to `posts/` with metadata, ready to publish

---

## 📦 Modules

Enable by telling the AI "I want to do [feature]" or by dropping a `.md` file in your config folder.

| Module | What it does |
|--------|-------------|
| **News Scout** | Discovers trending topics, cross-validates across sources |
| **Visual System** | Recommends the right image type for each post |
| **Memes** | Humor, roasts, meme formats with calibration levels |
| **Image Prompts** | Generates AI image prompts when no real image fits |
| **Video Content** | Short-form video specs, scripts, storyboards |
| **Carousel** | Multi-slide content creation |
| **Repurpose** | Adapts one post for multiple platforms |
| **Analytics** | Tracks what works, feeds insights back into the pipeline |

Don't need memes? Don't enable it. Want analytics later? Just ask.

---

## 📂 Project Structure

```
post-kit/
├── engine/
│   ├── core/           # Pipeline, onboarding, quality gates, anti-AI pass
│   ├── modules/        # Optional capabilities (news, memes, visuals, etc.)
│   └── platforms/      # Platform-specific rules (LinkedIn, X, etc.)
├── examples/
│   └── ai-tech/        # Complete working niche pack (study or copy)
├── my-niche/           # YOUR config lives here (created during setup)
├── posts/              # Generated posts go here
└── docs/               # Full documentation
```

---

## 🎯 Examples

The [`examples/ai-tech/`](examples/ai-tech/) folder contains a complete, proven niche pack for AI/tech content. It includes voice profile, content rules, sources, hashtags, and active modules — everything configured and working.

Use it to:
- Study how the pieces connect
- Copy it as a starting template for your own niche
- See what good configuration looks like

---

## 🤝 Contributing

We welcome contributions — especially:

- **Niche packs** — Share your working config for others in your niche
- **New modules** — Add capabilities anyone can use
- **Platform files** — Research and document new platforms
- **Anti-AI patterns** — Found a new AI tell? Add it

See [docs/contributing.md](docs/contributing.md) for guidelines.

---

## 🗺️ Roadmap

- [x] Core pipeline (Research → Write → Voice → Anti-AI → Quality Gate → Output)
- [x] Guided onboarding (10-question setup)
- [x] LinkedIn platform support
- [x] X (Twitter) platform support
- [x] 8 optional modules (news, memes, visuals, video, carousel, analytics, repurpose, image prompts)
- [ ] Community niche packs (fitness, crypto, SaaS, real estate, marketing)
- [ ] YouTube Community platform file
- [ ] Newsletter platform file
- [ ] Blog platform file
- [ ] Thread/series module (multi-post storylines)
- [ ] Scheduling integration suggestions (best time to post per platform)
- [ ] A/B hook testing (generate 3 hooks, pick the strongest)
- [ ] Voice calibration from existing posts (paste 5 posts, extract your voice automatically)

Have an idea? [Open a feature request](https://github.com/Huzaifa-ali/post-kit/issues/new?template=feature_request.md).

---

## 📄 License

[MIT](LICENSE) — use it however you want.
