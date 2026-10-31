---
name: responsive-layout-builder
description: Builds and audits responsive layouts across mobile, tablet, and desktop viewports. Enforces tri-breakpoint testing (390px, 768px, 1440px) to prevent horizontal overflow, cut-off content, and unreadable mobile controls. Use when styling views, fixing layout issues, or testing multi-device UI.
---

# Responsive Layout & Viewport Adaptation Protocol

> **Objective:** Ensure application user interfaces render seamlessly across smartphone screens, handheld kiosk tablets, and high-resolution desktop command centers with zero layout clipping or horizontal overflow.

---

## When to Use This Skill
- Creating new page templates, grids, sidebars, or modal dialogs.
- Diagnosing "RenderFlex overflowed", cut-off table columns, or mobile horizontal scrollbars.
- Optimizing web applications for mobile touch devices and handheld edge terminals.

---

## The Tri-Breakpoint Standard Matrix

Every layout must be audited against three standardized viewport widths:

| Breakpoint Tier | Width Target | Target Devices | Layout Geometry | Navigation Pattern |
| :--- | :--- | :--- | :--- | :--- |
| **Mobile Portrait** | `390px` – `480px` | iPhone / Android Phones | Single-column stack, full-width cards | Off-canvas sliding drawer or bottom bar |
| **Tablet / Kiosk** | `768px` – `1024px` | POS Terminals, iPads, Tablets | 2-column grid, compact KPI strip | Collapsible slim sidebar or top tab bar |
| **Desktop Command** | `1200px` – `1440px+`| Laptops, Workstations | Full multi-column dashboard grid | Centered floating shell with full sidebar |

---

## The 4-Step Responsive Audit Workflow

### Step 1: Enforce Root Viewport & Box Sizing
Ensure standard viewport and box-sizing rules are defined at the root level:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
```
```css
*, *::before, *::after {
  box-sizing: border-box;
}
html, body {
  overflow-x: hidden;
  max-width: 100vw;
}
```

### Step 2: Prevent Horizontal Table & Data Overflow
Data tables frequently break mobile screens. Enforce horizontal scrolling containers around data grids:
```css
.table-responsive-wrapper {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
```

### Step 3: Mobile Touch Target & Form Sizing
- Touch targets (buttons, select dropdowns, tab pills) must have a **minimum height and width of 44px**.
- Input font size must be at least `16px` on mobile to prevent iOS Safari auto-zooming on focus.

### Step 4: Fluid Typography & Spacing
- Use CSS `clamp()` for headings: `font-size: clamp(1.5rem, 4vw, 2.25rem);`.
- Use CSS Flexbox and Grid with `minmax()`: `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));`.
- Avoid hardcoded fixed pixel widths (`width: 600px;`) on container elements; use `max-width: 600px; width: 100%;`.
