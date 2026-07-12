# Contributing to post-kit

We welcome contributions from the community. Here's how you can help.

---

## Ways to Contribute

### 1. Share Your Niche Pack

If you've set up post-kit for your niche and it's working well, share it as an example for others.

**How:**
1. Copy your `my-niche/` files
2. Strip any personal information (real names, API keys, specific analytics data)
3. Add it to `examples/your-niche-name/`
4. Open a pull request

**What to include:**
- `niche.yaml` — your configuration
- `voice.md` — your voice profile
- `content-rules.md` — your posting rules
- `sources.md` — where you find content ideas
- `hashtags.yaml` — your hashtag strategy
- Any active module files (customized for your niche)

### 2. Add a New Module

Think of a capability that doesn't exist yet? Create it.

**How:**
1. Create a `.md` file in `engine/modules/`
2. Follow the pattern of existing modules:
   - Clear title and purpose
   - When to use / when not to use
   - Rules and guidelines
   - Output format
3. Open a pull request

**Module guidelines:**
- One capability per module
- Written in plain language (no jargon)
- Niche-agnostic (works for any topic area)
- Includes "when to use" and "when NOT to use" sections

### 3. Add a New Platform

Research a platform and document it.

**Requirements for a platform file:**
1. How the algorithm works (current, not outdated)
2. Ranking signals in priority order
3. Format specs (character limits, media sizes, video durations)
4. Best practices (timing, frequency, format choices)
5. What kills reach (common mistakes to avoid)
6. Platform-specific formatting rules
7. Anti-patterns specific to that platform

**Important:** Platform files should be based on real data and current algorithm knowledge, not generic advice. Cite sources where possible.

### 4. Improve Existing Files

Found something outdated, incorrect, or unclear? Fix it.

- Algorithm changes (platforms update constantly)
- Better examples
- Clearer wording
- Additional anti-AI patterns
- Bug fixes in the onboarding flow

---

## Pull Request Guidelines

- Keep changes focused (one PR per feature/fix)
- Explain what you changed and why
- If adding a niche pack, confirm it's actually been used (not hypothetical)
- If updating a platform file, cite your sources for algorithm claims
- Write in plain, accessible language
- No code, no JSON schemas, no technical jargon in user-facing files

---

## File Naming

- All lowercase
- Hyphens for spaces (not underscores)
- `.md` for instructions/rules
- `.yaml` for structured data (niche config, hashtags)

---

## What We Don't Accept

- Hypothetical niche packs nobody has tested
- Platform files based on outdated information (pre-2025)
- Modules that require code to function
- Anything that adds complexity for the end user
- AI-generated contributions that haven't been reviewed and tested

---

## Questions?

Open an issue on GitHub. We're friendly.
