# Update

Reconcile your niche with the latest post-kit improvements. Entirely opt-in — your customizations always win.

---

## When to Activate

Triggered by:
- "update my niche"
- "sync with post-kit"
- "what changed in post-kit"
- "check for updates"
- The version notice at pipeline start (user follows the prompt)

---

## How It Works

### Step 1: Detect Version Gap

1. Read the `VERSION` file at the project root → this is the **current post-kit version**.
2. Read `my-niche/niche.yaml` → look for the `postkit_version` field → this is the **user's version**.
3. If `postkit_version` is missing, the user set up before the update system existed. Treat their version as `"0.0.0"` (pre-update-system).
4. If versions match → say "You're up to date!" and stop.
5. If user's version is behind → proceed to Step 2.

### Step 2: Identify What Changed

Read the `CHANGELOG.md` and identify all changes between the user's version and the current version.

Classify changes into two buckets:

**Engine changes (automatic, informational only):**
- Changes to `engine/core/*` files (anti-ai-writing, quality-gates, pipeline, web-research, brainstorm, onboarding)
- Changes to `engine/platforms/*` files
- These already took effect when post-kit was updated — just inform the user what's new.

**Module template changes (opt-in):**
- Changes to `engine/modules/*` files
- These only matter if the user has a corresponding file in `my-niche/`
- The user's copy is independent — upstream changes DON'T auto-apply.

### Step 3: Report Engine Changes

Present engine changes briefly:

> "Since your last sync, the post-kit engine updated:
>
> - [list key changes, 1 line each]
>
> These are already active — they're part of the framework. No action needed from you."

### Step 4: Reconcile Module Changes

For each changed engine module template where the user has a corresponding `my-niche/` file:

1. Read the **engine template** (`engine/modules/<module>.md`) — the new version.
2. Read the **user's file** (`my-niche/<module>.md`) — their customized version.
3. Compare them and identify:
   - **New sections** in the template that don't exist in the user's file
   - **Changed guidance** where the template's approach evolved
   - **Removed/deprecated** patterns the template no longer recommends
4. Present each difference conversationally:

> "**image-prompts.md** — the template added a new 'Negative prompt' section that wasn't there when you set up. Your file doesn't have it.
>
> Want me to add it to your file? Your existing customizations stay untouched — I'd just append the new section.
>
> [Yes / No / Show me what it looks like first]"

**Rules for reconciliation:**
- Present ONE module at a time. Don't dump everything at once.
- Always show what would change BEFORE applying it.
- Never overwrite existing content the user customized — only add, never replace.
- If the template changed something the user ALSO customized differently, say so honestly: "The template now recommends X, but you have Y. Your version stays — just flagging it in case you want to revisit."
- The user can say "skip" or "no" to any individual change. Respect it silently.

### Step 5: Handle Modules the User Doesn't Have

If a new module was added to `engine/modules/` that didn't exist when the user set up:

> "New module available: **[module name]** — [one line description]. Want me to set it up for you?"

Only mention it. Don't push. The user activates modules by choice.

### Step 6: Stamp the Version

After going through all changes (whether the user accepted any or not):

1. Update `postkit_version` in `my-niche/niche.yaml` to the current `VERSION`.
2. Confirm:

> "Done — your niche is marked as synced to post-kit [version]. Next time post-kit updates, I'll let you know what's new."

---

## Handling Pre-Update-System Users

If `postkit_version` is missing from `my-niche/niche.yaml`:

1. Add the field to their `niche.yaml` (set to current VERSION).
2. Don't try to reconcile every historical change — that's overwhelming and pointless.
3. Instead, do a quick scan:

> "Your niche was set up before the update system. I've added version tracking now.
>
> Want me to do a quick check of your module files against the current templates to see if there's anything useful you're missing? Or just start fresh from here?"

If they say yes, run Step 4 for all their active modules. If no, just stamp and move on.

---

## What This Skill NEVER Does

- Never overwrites user content without explicit approval
- Never changes `voice.md` or identity sections of `niche.yaml`
- Never auto-applies module changes
- Never removes user customizations
- Never touches files in `my-niche/` that have no engine template counterpart (custom modules like `github-screenshot.md` are immune)
- Never forces an update — the user can always say "not now" and the version stays where it was until they're ready

---

## Conflict Philosophy

When the engine template and the user's file disagree:

| Situation | Action |
|---|---|
| Template added something new, user's file doesn't have it | Offer to add it (append, never replace) |
| Template changed approach, user kept the old way | Inform only — "template now does X, you have Y, keeping yours" |
| Template removed/deprecated something, user still has it | Mention it: "template dropped X, you still have it — remove?" |
| User has something the template doesn't | Leave it alone completely — it's their customization |

**The user's file is THEIR file.** The engine template is a reference, not an authority over their niche.

---

## Example Flow

```
User: "update my niche"

Agent: [reads VERSION → 1.2.0, reads niche.yaml → postkit_version: "1.0.0"]

Agent: "You're on post-kit 1.0.0, current is 1.2.0. Here's what changed:

**Engine (already active):**
- anti-ai-writing.md: 8 new banned words added (leverage, synergy, etc.)
- quality-gates.md: hook-strength gate now checks for specific numbers in first line
- linkedin.md: updated algorithm weights based on 2026 Q3 data

**Your modules — want to review?**
- image-prompts template evolved (new negative-prompt section)
- news-scout template added a 'skip if' checklist

Want me to walk through the module changes one by one?"

User: "yeah go ahead"

Agent: "First up — image-prompts.md.

The template added a 'Negative prompt' block — a standard set of things to exclude
from every AI image (no misspelled text, no watermarks, no cluttered composition).

Your file doesn't have this. Want me to append it at the end of your image-prompts.md?
Your existing 3-prompt system and all customizations stay exactly as they are.

[Yes / No / Show me the block first]"

User: "yes"

Agent: [appends the section, moves to next module]
```

---

## Integration

This skill is referenced from:
- `pipeline.md` — version notice at pipeline start triggers awareness
- `AGENTS.md` — listed as a user command ("update my niche" / "check for updates")
- `POWER.md` — mentioned in steering instructions
