# Platforms

post-kit supports multiple platforms. LinkedIn is the default. You can add more during setup or anytime after.

---

## Supported Platforms

| Platform | File | Status |
|----------|------|--------|
| LinkedIn | `engine/platforms/linkedin.md` | Fully documented (proven) |
| X (Twitter) | `engine/platforms/x.md` | Documented |
| YouTube Community | `engine/platforms/youtube-community.md` | Coming soon |
| Newsletter | `engine/platforms/newsletter.md` | Coming soon |
| Blog | `engine/platforms/blog.md` | Coming soon |

---

## How Platforms Work

Each platform file contains:
- How the algorithm works
- What signals drive reach
- Format and character limits
- Best practices (posting time, frequency)
- What kills reach on that platform
- Platform-specific formatting rules

The AI reads the relevant platform file when writing your post and adapts content accordingly.

---

## Using Multiple Platforms

You can have one or more platforms active. Set them in your `my-niche/niche.yaml`:

```yaml
platforms:
  - linkedin
  - x
```

When you write a post, the AI will either:
- Write for your primary platform, or
- Ask if you want adapted versions for each platform

Use the **repurpose module** if you regularly want multi-platform output.

---

## Switching Platforms

To change your active platform(s):
- Edit the `platforms:` list in `my-niche/niche.yaml`
- Or tell the AI: "I want to add X/Twitter to my platforms"

---

## Contributing a Platform

Want to add a new platform (TikTok captions, Threads, Reddit, etc.)? See [contributing.md](contributing.md) for guidelines. Each platform file needs:

1. Algorithm explanation (how reach works)
2. Ranking signals (what the platform rewards)
3. Format specs (character limits, media sizes)
4. Best practices (timing, frequency, format)
5. What kills reach (common mistakes)
6. Platform-specific patterns to avoid
