---
name: frontend-design
description: Enforces professional, bespoke frontend aesthetics and anti-AI slop design standards. Uses curated color tokens, editorial typography, tactile micro-interactions, and WCAG AA accessibility. Use when building UI components, styling layouts, creating dashboards, or modernizing web applications.
---

# Anti-AI Slop Frontend Design Protocol

> **Objective:** Eliminate generic, uninspired AI output (clashing dark modes, neon purple borders, browser default fonts) by enforcing an institutional, bespoke design standard.

---

## When to Use This Skill
- Designing any web application, dashboard, or customer-facing interface.
- Creating or refactoring CSS design systems, tokens, or layouts.
- Reviewing UI components for accessibility, aesthetics, and responsiveness.

---

## The 5 Pillars of Anti-AI Slop Design

### 1. Curated Palette vs. Random Colors
- Never use raw default colors (plain `#ff0000`, `#0000ff`, or uncalibrated neon purples).
- Use an institutional, harmonious palette defined in CSS variables:
  - **Canvas Background:** Soft ivory/cream (`#fbfbf7` / `#f5f6f0`) or calibrated slate (`#0f172a`).
  - **Typography:** Deep forest green (`#214239`) or deep charcoal (`#1e293b`).
  - **Accents:** Natural sage (`#789085`) and rich emerald (`#166c52`).
  - **Status Hues:** Warm amber (`#d97706`), rose red (`#b91c1c`).
- Ensure all text-to-background combinations achieve a **minimum contrast ratio of 4.5:1 (WCAG AA)**.

### 2. Editorial Typography Pairing
- **Never rely on unconfigured browser default fonts.**
- Pair an authoritative serif heading font with a crisp data sans-serif:
  - *Headings & Titles:* `Newsreader`, `Fraunces`, or `Merriweather` (provides a bespoke, human, authoritative feel).
  - *Data Tables, Labels & Inputs:* `Inter`, `Geist`, or `Outfit` (clean geometric legibility).
  - *Codes, Hashes & Nonces:* `JetBrains Mono` or `Consolas`.

### 3. Surface Harmonization & Shell Geometry
- Avoid jarring contrast clashes (e.g. placing a jet-black cyberpunk sidebar directly against a soft cream content card).
- Use frosted glass surface cards:
  ```css
  background: rgba(255, 255, 255, 0.88);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(226, 230, 220, 0.95);
  box-shadow: 0 8px 30px rgba(40, 54, 48, 0.05);
  border-radius: 16px;
  ```

### 4. Tactile Micro-Interactions
- Every interactive element (button, tab, row, input) must feel alive:
  - Subtle hover lift: `transform: translateY(-1px);`
  - Active press: `transform: scale(0.99);`
  - Smooth transitions: `transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);`
- Use animated skeleton loaders while fetching data instead of leaving empty white boxes.

### 5. Layout Stability & Zero Overflows
- Center the main shell inside a bounded grid: `max-width: 1440px; margin: 16px auto;`.
- Ensure independent scrolling for sidebars and content panes with custom slim 4px scrollbars.
