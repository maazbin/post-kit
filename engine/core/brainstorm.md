# Brainstorm

Activate this when the user wants to improve any part of their content pipeline. This is not about writing posts — it's about making the PIPELINE ITSELF better.

---

## When to Activate

Triggered by:
- "My hooks aren't working"
- "Help me improve my voice"
- "My posts aren't getting engagement"
- "Let's refine my content rules"
- "I want to change my approach to [X]"
- "Help me improve my [any pipeline component]"
- "Let's brainstorm about my pipeline"
- "Make my pipeline better"

---

## How It Works

### Step 1: Identify What to Improve

Ask: "Which part of your pipeline do you want to work on?"

If they already said (e.g., "my hooks"), skip this and go to Step 2.

Options to offer if they're unsure:
- Voice (how you sound)
- Hooks (how your posts open)
- Content rules (what you post, structure, length)
- Visual approach (how you handle images)
- Meme/humor style (your comedy approach)
- Sources (where you find topics)
- Hashtag strategy
- Anything else — just describe it

### Step 2: Understand the Problem

Read the relevant file from `my-niche/`. Then ask:

- "Here's what your current [voice/hooks/rules] look like: [brief summary]"
- "What's not working about it? What do you wish was different?"

Listen to their answer. Ask follow-up questions if needed to understand the gap between current state and desired state.

### Step 3: Propose Approaches

Offer 2-3 concrete alternative approaches. Not vague suggestions — show them what the REWRITTEN instructions would look like.

Example:
> "Here are 3 directions we could take your hooks:
>
> **Option A: Lead with numbers**
> Every hook opens with a specific data point. '$X for Y', '3 things wrong with Z', '80% of people miss this.'
>
> **Option B: Lead with disagreement**
> Every hook states a contrarian opinion immediately. 'Everyone's wrong about X', 'Stop doing Y', 'X is overrated.'
>
> **Option C: Lead with story**
> Every hook opens mid-moment. 'I was in a meeting when...', 'Yesterday something broke', 'Three months ago I made a mistake.'
>
> Which direction resonates? Or mix elements from multiple?"

### Step 4: Implement the Change

Once they pick (or customize), rewrite the relevant file in `my-niche/` with the new instructions.

Show them the before/after:
> "Here's what changed in your [file]:
> 
> Before: [old approach]
> After: [new approach]
>
> Want me to adjust anything?"

### Step 5: Confirm

> "Done. Your pipeline is updated. Next post will use these new rules. Want to test it now with a post, or anything else to improve?"

---

## Rules

- Always READ the current file before suggesting changes
- Never suggest changes without understanding what's NOT working
- Show concrete examples, not vague advice
- Only change the file they asked about — don't touch other files unless they ask
- If their problem is actually a different file (e.g., they say "my hooks" but the issue is their voice), suggest looking at the right file first
- Keep suggestions within their niche and style — don't try to turn a professional creator into a meme account unless they ask

---

## Adding New Modules

If during brainstorming the user says they want a capability that requires a module they don't have:

> "That sounds like you'd benefit from the [module name] module. It handles [what it does]. Want me to set it up for you?"

If yes, read the module template from `engine/modules/`, ask any module-specific setup questions, and generate the customized version in `my-niche/`.

---

## Changing Niche

If the user wants to change their entire niche:

> "Want to start fresh with guided setup for your new niche, or keep your current structure and just update the topic/pillars?"

- **Fresh:** Clear my-niche/ files and rerun the guided onboarding
- **Update:** Edit niche.yaml, voice.md, sources.md, and hashtags.yaml to reflect the new niche while keeping the same structural rules
