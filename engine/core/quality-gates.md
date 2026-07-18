# Quality Gates

Every post must pass ALL of these gates before it's delivered to the user. If it fails any gate, revise and re-check.

---

## Gate 1: Hook Strength

The first 1-2 lines must make someone want to read more.

**Pass if:**
- Opens with a specific claim, number, opinion, or question
- Creates curiosity or tension
- Would make YOU stop scrolling

**Fail if:**
- Opens with generic context-setting ("In the world of...")
- First line could apply to any topic
- No reason to keep reading

---

## Gate 2: One Idea Rule

A post should have one clear idea. Not two. Not three.

**Pass if:**
- You can summarize the post's point in one sentence
- Everything in the post supports that one point
- Nothing feels tangential or "also..."

**Fail if:**
- The post tries to cover multiple topics
- There's a "Also worth mentioning..." section
- Reader would be confused about the main takeaway

---

## Gate 3: Personal Opinion

Every post needs at least one genuine personal take.

**Pass if:**
- Contains a direct opinion ("I think...", "This is dumb", "Nobody's talking about...")
- The opinion is specific enough that someone could disagree
- It reflects the voice in voice.md

**Fail if:**
- Pure information delivery with no stance
- Opinions are hedged into meaninglessness ("It could be argued that...")
- Opinion is so generic nobody could disagree ("Quality matters")

---

## Gate 4: Save or Share Test

The post must pass at least one of these:

- **Save test:** "Would someone bookmark this because they'll want to reference it later?"
  - Has specific numbers, frameworks, comparisons, or actionable advice
- **Share test:** "Would someone send this to a friend or colleague?"
  - Has a strong opinion, surprising take, or entertaining angle

**Fail if:** Neither. It's informative but forgettable. Rewrite with a stronger angle.

---

## Gate 5: Anti-AI Cleanliness

The post must have passed through `engine/core/anti-ai-writing.md` with zero violations remaining.

**Pass if:**
- No banned words
- No banned patterns
- Em dashes used sparingly (max ~2 per post) — part of the real voice, but not stacked or used as a crutch
- Doesn't read like AI output
- Has personality and irregular rhythm
- Uses contractions naturally (don't, won't, it's)

**Fail if:** Any banned word or pattern remains, OR more than ~2 em dashes appear, OR the "it's not X — it's Y" reframe shows up more than once. Run anti-AI pass again.

**Common miss:** Em dashes stack up fast. Count them. Two is fine (it's the voice). Three or more, cut the weakest to a period or comma. The reframe inversion belongs in the quoted-opinion line only, not every paragraph.

---

## Gate 6: Pillar Alignment

Every post must map to one of the content pillars defined in `my-niche/niche.yaml`.

**Before checking this gate:** Read `my-niche/niche.yaml` and extract the user's `content_pillars` list. Use ONLY those pillar names — never hardcode or assume pillars.

**Pass if:**
- The post clearly belongs to one pillar from the user's niche.yaml
- The post's metadata/front-matter labels it correctly using a pillar that EXISTS in niche.yaml
- The tone matches the pillar's described purpose

**Fail if:**
- Post uses a pillar name that doesn't exist in the user's niche.yaml
- Post doesn't fit any of the user's defined pillars — it's off-topic for the account
- Post tries to span multiple pillars without committing to one angle

**Why this matters:** Platform algorithms reward topic authority. Off-pillar posts dilute your semantic signal. If you want to expand pillars, update niche.yaml FIRST, then post.

---

## Gate 7: Platform Compliance

The post must follow the active platform's rules.

**Check against the relevant platform file:**
- Character count within limits?
- Format appropriate for the platform?
- Links handled correctly (in body vs. in comments)?
- Hashtag count and placement correct?

---

## Gate 8: Length Check

Compare against the length rules in `my-niche/content-rules.md`.

- Is it within the specified character/line count for this post type?
- Is it long enough? Short posts (under ~800 chars) underperform unless it's a meme/visual post.
- If the visual carries the content, is the text SHORT?
- No unnecessary padding or filler?

---

## Scoring (Optional)

If the user has analytics.md active, also check:
- Does this topic align with what's historically performed well?
- Is the format/angle similar to past high-performers?

This is informational, not a hard gate. Don't kill a good post because analytics say the topic is untested.

---

## If a Post Fails

1. Identify which gate(s) failed
2. Revise the post targeting those specific failures
3. Re-run from Voice Pass (Step 3 in pipeline) to catch any new issues introduced
4. Re-check all gates

If a post fails the same gate 3 times, flag it to the user:
> "This post is struggling with [gate]. Here's the issue: [explain]. Want me to try a completely different angle, or should I work with what we have?"
