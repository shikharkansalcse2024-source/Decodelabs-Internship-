# Project 1 — AI-Generated Cyberpunk Brand Asset Kit

> Cybersecurity Startup Rebranding using AI Image Generation and Advanced Prompt Engineering

---

## Problem Statement

A high-end cybersecurity tech startup required unique visual assets for website and social media rebranding. Stock photos were too generic and failed to communicate the brand's positioning. The startup needed a consistent **Cyberpunk-Corporate** aesthetic across all assets.

---

## Objectives

- Generate 5 high-quality, brand-consistent visual assets using AI
- Apply advanced prompting techniques (negative prompts, aspect ratios, lighting styles)
- Maintain visual consistency across all generated assets
- Deliver production-ready assets for web and social media use

---

## Brand Style Guide

| Attribute | Specification |
|-----------|--------------|
| Aesthetic | Cyberpunk-Corporate |
| Primary Color | Neon Blue `#00f0ff` |
| Secondary Color | Electric Purple `#9b00ff` |
| Background | Dark Navy `#0a0a2e` |
| Accent | Chrome Silver `#c0c0c0` |
| Mood | Futuristic, powerful, mysterious, trustworthy |
| Lighting | Neon rim lighting, volumetric glow, lens flares |
| Avoid | Warm colors, cartoons, nature, watermarks |

---

## Assets Delivered

### Asset 1 — Logo Concept
![Logo](./06-Final-Assets/logo-v2-square-FINAL.png)

| Property | Value |
|----------|-------|
| Tool | DALL-E 3 (ChatGPT) |
| Aspect Ratio | 1:1 Square |
| Description | Geometric shield with symmetric circuit tree pattern, neon blue/purple dual-tone, chrome metallic border |

---

### Asset 2 — Hero Image
![Hero](./06-Final-Assets/hero-image-v1-FINAL.png)

| Property | Value |
|----------|-------|
| Tool | DALL-E 3 (ChatGPT) |
| Aspect Ratio | 16:9 Landscape |
| Description | Cinematic server room, hooded figure, floating holographic shields, volumetric neon lighting, reflective floor |

---

### Asset 3 — Icon Set

| Icon | Image | Description |
|------|-------|-------------|
| Shield | ![Shield](./06-Final-Assets/icon-1-shield-FINAL.png) | Circuit tree pattern, blue-purple split |
| Lock | ![Lock](./06-Final-Assets/icon-2-lock-FINAL.png) | Radial circuits from keyhole center |
| Eye | ![Eye](./06-Final-Assets/icon-3-eye-FINAL.png) | Surveillance eye with circuit iris |

---

## Prompt Engineering Techniques

### 1. Positive Prompting
Detailed structured prompts using the formula:
```
[Subject] + [Style] + [Colors] + [Lighting] + [Mood] + [Technical Specs]
```

### 2. Negative Prompting
Every generation included explicit avoidance instructions:
```
Avoid: cartoon, warm colors, hand-drawn, sketchy,
watermark, text, blurry, low quality, anime
```

### 3. Aspect Ratio Control
```
Logo & Icons  → 1:1  (Square)
Hero Image    → 16:9 (Wide Landscape)
```

### 4. Style Anchor Technique
Added to every icon prompt to maintain consistency without Img2Img:
```
"same style as a glowing cyberpunk shield icon,
neon blue and electric purple, dark navy background,
chrome metallic border, circuit pattern details"
```

### 5. Iterative Refinement
```
Generate → Review → Identify Issues → Refine Prompt → Regenerate
```

---

## All Prompts

### Logo Concept
**Positive:**
```
A minimalist cybersecurity company logo concept, featuring a
geometric shield with a glowing circuit pattern inside,
cyberpunk aesthetic, neon blue and electric purple color palette,
dark navy background, chrome metallic edges, holographic glow
effect, clean professional design, ultra sharp, 4K, perfectly
square 1:1 composition, centered subject with equal padding on
all sides, no text, no watermark
```
**Negative:**
```
Avoid: cartoon style, warm colors, hand-drawn look, sketchy
lines, blurry edges, watermark, text, letters, portrait format
```

---

### Hero Image
**Positive:**
```
A cinematic wide-angle hero image for a cybersecurity company
website, a lone hooded hacker figure standing in a vast dark
server room, surrounded by floating holographic shields and
glowing blue circuit patterns, volumetric neon blue and purple
lighting, reflective floor, dramatic rim lighting,
cyberpunk-corporate aesthetic, ultra realistic,
8K resolution, 16:9 aspect ratio, no text, no watermark
```
**Negative:**
```
Avoid: warm lighting, daylight, nature backgrounds, cartoon,
low quality, blurry, crowded composition, stock photo look,
watermark, text
```

---

### Icon 1 — Shield
**Positive:**
```
A glowing cybersecurity shield icon, flat design,
neon blue and electric purple equal glow, dark navy
background, symmetric circuit pattern inside shield,
metallic chrome border, holographic effect,
minimalist professional design, sharp clean edges,
perfectly square 1:1 composition, 4K, no text, no watermark
```
**Negative:**
```
Avoid: cartoon, warm colors, hand-drawn, sketchy,
watermark, text, blurry, low quality, anime, manga
```

---

### Icon 2 — Lock
**Positive:**
```
A glowing cybersecurity padlock icon, same style as
a glowing cyberpunk shield icon, neon blue and electric
purple, dark navy background, chrome metallic border,
circuit pattern details, holographic glow effect,
minimalist flat design, sharp clean edges, perfectly
square 1:1 composition, 4K, no text, no watermark
```
**Negative:**
```
Avoid: cartoon, warm colors, hand-drawn, sketchy,
watermark, text, blurry, low quality, anime, manga
```

---

### Icon 3 — Eye
**Positive:**
```
A glowing surveillance eye icon for a cybersecurity brand,
same style as a glowing cyberpunk shield icon, neon blue
and electric purple, dark navy background, chrome metallic
border, circuit pattern details, neon blue iris with circuit
pattern inside, holographic glow around edges, minimalist
flat design, perfectly square 1:1 composition, 4K,
no text, no watermark
```
**Negative:**
```
Avoid: cartoon, warm colors, hand-drawn, sketchy,
watermark, text, blurry, low quality, anime,
creepy, horror style, bloodshot
```

---

## Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| First logo generated in portrait orientation | Added explicit square composition instructions to prompt |
| DreamStudio redirected to Brand Studio | Explored Tensor.art; adopted Style Anchor Technique on DALL-E 3 |
| Maintaining icon consistency without Img2Img | Developed Style Anchor line added to every icon prompt |

---

## Brand Consistency Score

| Criteria | Logo | Hero | Shield | Lock | Eye |
|----------|------|------|--------|------|-----|
| Neon Blue + Purple | ✓ | ✓ | ✓ | ✓ | ✓ |
| Dark Navy Background | ✓ | ✓ | ✓ | ✓ | ✓ |
| Chrome Metallic Border | ✓ | ✓ | ✓ | ✓ | ✓ |
| Circuit Pattern | ✓ | ✓ | ✓ | ✓ | ✓ |
| Holographic Glow | ✓ | ✓ | ✓ | ✓ | ✓ |
| Correct Aspect Ratio | ✓ | ✓ | ✓ | ✓ | ✓ |
| No Text/Watermark | ✓ | ✓ | ✓ | ✓ | ✓ |

**Overall Consistency: 100%**

---

## Tools Used

| Tool | Purpose |
|------|---------|
| DALL-E 3 (ChatGPT) | Primary image generation |
| Tensor.art | Explored for Img2Img workflow |

---

## Folder Structure

```
Project-1-Cyberpunk-Brand-Assets/
├── 01-Brand-Guide/
│   └── brand-style-guide.txt
├── 02-Prompts/
│   └── all-prompts.txt
├── 03-Logo-Concepts/
│   ├── logo-v1-portrait.png
│   ├── logo-v2-square-FINAL.png
│   └── logo-v3-dramatic.png
├── 04-Hero-Image/
│   └── hero-image-v1-FINAL.png
├── 05-Icons/
│   ├── icon-1-shield-FINAL.png
│   ├── icon-2-lock-FINAL.png
│   └── icon-3-eye-FINAL.png
├── 06-Final-Assets/
│   ├── logo-v2-square-FINAL.png
│   ├── hero-image-v1-FINAL.png
│   ├── icon-1-shield-FINAL.png
│   ├── icon-2-lock-FINAL.png
│   └── icon-3-eye-FINAL.png
└── README.md
```

---

## Key Learnings

- Prompt quality directly drives output quality
- Negative prompts are equally important as positive prompts
- Style Anchor Technique effectively replaces Img2Img for consistency
- Aspect ratio must always be explicitly specified
- Iterative refinement consistently produces better results

---

*Completed: June 2026 | AI/ML Internship Program*
