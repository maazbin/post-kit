"""Onboarding route — guided setup wizard."""

from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse

import yaml

from .helpers import templates, MY_NICHE_DIR, is_setup_complete

router = APIRouter()


@router.get("/onboarding")
async def onboarding_page(request: Request):
    if is_setup_complete():
        return RedirectResponse(url="/dashboard", status_code=302)

    return templates.TemplateResponse(request, "onboarding.html", {
        "page": "onboarding",
    })


@router.post("/onboarding")
async def onboarding_submit(
    request: Request,
    niche: str = Form(...),
    voice: str = Form("Casual and friendly"),
    voice_custom: str = Form(""),
    platforms: str = Form("linkedin"),
    pillars: str = Form("General content 100%"),
    visuals: str = Form("no"),
    humor: str = Form("no"),
    content_style: str = Form("mix"),
    audience_hangouts: str = Form(""),
    cadence: str = Form("3-5 times a week"),
    timezone: str = Form("Asia/Karachi"),
):
    """Process onboarding form and generate config files."""
    # Ensure my-niche directory exists
    MY_NICHE_DIR.mkdir(parents=True, exist_ok=True)

    # Parse pillars into structured data
    pillar_list = []
    for line in pillars.strip().split("\n"):
        line = line.strip().strip("-").strip()
        if line:
            # Try to parse "Topic 40%" format
            parts = line.rsplit(" ", 1)
            if len(parts) == 2 and parts[1].replace("%", "").isdigit():
                pillar_list.append({
                    "name": parts[0].strip(),
                    "percentage": int(parts[1].replace("%", ""))
                })
            else:
                pillar_list.append({"name": line, "percentage": 0})

    # Normalize percentages if they don't add up
    total_pct = sum(p["percentage"] for p in pillar_list)
    if total_pct == 0 and pillar_list:
        even_split = 100 // len(pillar_list)
        for p in pillar_list:
            p["percentage"] = even_split

    # Build niche.yaml
    platform_list = [p.strip() for p in platforms.split(",")]
    niche_data = {
        "name": niche,
        "identity": {
            "description": f"{niche} content creator",
            "personality": voice_custom if voice == "custom" else voice,
        },
        "platforms": platform_list,
        "content_pillars": pillar_list,
        "cadence": {
            "frequency": cadence,
            "timezone": timezone,
        },
        "modules_active": [],
    }

    # Determine active modules
    if visuals.lower() == "yes":
        niche_data["modules_active"].append("visual-system")
    if humor.lower() == "yes":
        niche_data["modules_active"].append("memes")
    if content_style.lower() in ("news-based", "mix"):
        niche_data["modules_active"].append("news-scout")

    # Write niche.yaml
    with open(MY_NICHE_DIR / "niche.yaml", "w", encoding="utf-8") as f:
        yaml.dump(niche_data, f, default_flow_style=False, allow_unicode=True)

    # Write voice.md
    voice_label = voice_custom if voice == "custom" else voice
    voice_content = f"""# Voice Profile

## Sound Like
{voice_label}

## Rules
- First-person, conversational
- State opinions directly
- Short punchy sentences
- No corporate speak
- Be authentic and real

## Never Sound Like
- Corporate press release
- AI trying to sound human
- Generic motivational speaker
- Engagement farming influencer
"""
    with open(MY_NICHE_DIR / "voice.md", "w", encoding="utf-8") as f:
        f.write(voice_content)

    # Write content-rules.md
    content_rules = f"""# Content Rules

## Structure

```
[Hook — 1-2 lines]
[Body]
[CTA — drives comments or shares]
```

## Mandatory Rules
- ONE idea per post
- Hook in first 2 lines
- Short sentences, short paragraphs
- Include one genuine personal opinion
- End with a CTA that invites discussion
- Pass: "Would someone save this?" OR "Would someone share this?"

## Content Style
{content_style}

## Pillars
"""
    for p in pillar_list:
        content_rules += f"- {p['name']} ({p['percentage']}%)\n"

    with open(MY_NICHE_DIR / "content-rules.md", "w", encoding="utf-8") as f:
        f.write(content_rules)

    # Write sources.md
    sources_content = f"""# Sources

## Where Your Audience Hangs Out
{audience_hangouts}

## Source Tiers
- Tier 1 (official announcements): share freely
- Tier 2 (press/reporting): attribute
- Tier 3 (blogs/newsletters): add context
- Tier 4 (social media claims): verify first
"""
    with open(MY_NICHE_DIR / "sources.md", "w", encoding="utf-8") as f:
        f.write(sources_content)

    # Generate optional module files
    engine_modules = MY_NICHE_DIR.parent / "engine" / "modules"

    if visuals.lower() == "yes" and (engine_modules / "visual-system.md").exists():
        content = (engine_modules / "visual-system.md").read_text(encoding="utf-8")
        (MY_NICHE_DIR / "visual-system.md").write_text(content, encoding="utf-8")

    if humor.lower() == "yes" and (engine_modules / "memes.md").exists():
        content = (engine_modules / "memes.md").read_text(encoding="utf-8")
        (MY_NICHE_DIR / "memes.md").write_text(content, encoding="utf-8")

    if content_style.lower() in ("news-based", "mix"):
        if (engine_modules / "news-scout.md").exists():
            content = (engine_modules / "news-scout.md").read_text(encoding="utf-8")
            (MY_NICHE_DIR / "news-scout.md").write_text(content, encoding="utf-8")

    return RedirectResponse(url="/dashboard", status_code=302)
