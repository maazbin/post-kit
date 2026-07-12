# Image Prompts Module

Handles AI image generation when no real screenshot, stock photo, or meme fits the post. Provides multiple prompt options exploring different visual angles.

---

## When to Use AI Images

LAST RESORT. Only when:
- No real screenshot exists for the topic
- No stock photo captures the feeling
- The post NEEDS a visual that doesn't exist in reality
- The user specifically wants AI-generated imagery

NEVER use when:
- A real screenshot IS the content
- A sourced meme carries the emotion better
- The post works as text-only
- Stock footage would be more authentic

---

## The Multi-Prompt System

Every post needing AI images gets **4 prompts** exploring DIFFERENT visual angles. The user picks the one they like best and generates it themselves.

### Why 4?
- More options = better chance of a great image
- Each explores a different creative direction
- One safe + one risky minimum
- User has creative control in the final choice

---

## Prompt Formula

```
[Subject] + [Setting] + [Style] + [Lighting] + [Camera angle] + [Color/Mood]
```

**Rules:**
- Maximum 60 words per prompt
- ONE specific detail from the post (a number, company name, price)
- ONE accent color
- ONE light source
- ONE lens/camera reference
- Always photorealistic (unless user's niche calls for illustration)
- Never: illustration, cartoon, flat design, even lighting, blue-purple gradients

---

## Angle Categories

Use different angle categories based on what the post is about:

### For pricing/cost content:
1. Cinematic Number — the number is the hero in a dramatic scene
2. Victim POV — person reacting, screen glow, shock on face
3. Physical Metaphor — burning money, overflowing meter, broken piggybank
4. Absurdist Scale — the number on a billboard, mountain, building

### For product/tool launches:
1. Power Reveal — product glowing, dominant in frame
2. Before/After Split — old decayed vs new pristine
3. Scale of Impact — tiny humans, enormous product
4. Environment Disruption — normal scene with one impossible element

### For drama/controversy:
1. Caught in the Act — absurdist candid scene
2. Corporate Contradiction — split showing say vs do
3. Dark Comedy — noir lighting, tension
4. Ironic Trophy — award/plaque/statue for failure

### For humor/memes:
1. Staged Absurdity — ridiculous scene, deadpan delivery
2. Ironic Juxtaposition — things that shouldn't coexist
3. Fake Document — realistic sign/menu saying absurd thing
4. Emotional Extreme — exaggerated reaction

### For opinion/hot takes:
1. Bold Text Card — dark background, strong typography only
2. Lone Voice — single person against vast backdrop
3. Visual Disagreement — something clearly wrong, nobody noticing
4. Confrontation — opposing elements face-to-face

### For comparisons:
1. Split Arena — left vs right, cool vs warm tones
2. David vs Goliath — size difference
3. Competition — physical opponents
4. Crossroads — two doors, two paths

---

## Quality Rules

1. Each of 4 prompts must produce a DIFFERENT-looking image
2. Minimum one safe/clean option + one risky/creative option
3. Label each prompt with its angle name
4. First prompt = most likely to perform well
5. Include the key post detail (number/name/price) in at least 2 of 4

---

## Output Format

```markdown
## Image Prompts
**Type:** AI-generated
**Status:** Prompts ready for user to generate

**Prompt 1 — [Angle Name]:**
[60 words max]

**Prompt 2 — [Angle Name]:**
[60 words max]

**Prompt 3 — [Angle Name]:**
[60 words max]

**Prompt 4 — [Angle Name]:**
[60 words max]

Pick your favorite and generate with your preferred AI image tool.
```
