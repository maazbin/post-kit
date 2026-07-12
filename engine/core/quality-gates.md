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
- Doesn't read like AI output
- Has personality and irregular rhythm

**Fail if:** Any banned word or pattern remains. Run anti-AI pass again.

---

## Gate 6: Platform Compliance

The post must follow the active platform's rules.

**Check against the relevant platform file:**
- Character count within limits?
- Format appropriate for the platform?
- Links handled correctly (in body vs. in comments)?
- Hashtag count and placement correct?

---

## Gate 7: Length Check

Compare against the length rules in `my-niche/content-rules.md`.

- Is it within the specified word/line count for this post type?
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
