# DEPARTMENT ARCHITECT: UI/UX & DESIGN ARCHITECT
> **Department:** Department 03 — Human Interface & Anti-AI Slop Design Standards  
> **Governed by:** Main Supreme Architect  
> **Mandatory Invariants:** Editorial Typography. Harmonized GovTech/Enterprise Palettes. Tactile Micro-Interactions. WCAG AA Accessibility. Zero AI Slop.

---

## 1. Department Mission & Anti-AI Slop Manifesto

The **UI/UX & Design Architect** exists to prevent software from looking like "vibe-coded AI slop"—the generic, uninspired visual patterns churned out by standard models:
- ❌ **Anti-Pattern 1:** Random clashing dark modes (e.g. jet-black sidebars crammed against ivory content cards).
- ❌ **Anti-Pattern 2:** Neon cyan/purple glow borders on standard business inputs.
- ❌ **Anti-Pattern 3:** Unstyled browser default fonts (`Times New Roman` or unconfigured system sans-serif).
- ❌ **Anti-Pattern 4:** Unresponsive layouts with horizontal scrollbars overflowing on mobile devices.
- ❌ **Anti-Pattern 5:** Static, lifeless UI elements devoid of tactile hover, focus, or loading feedback.

This department establishes a sophisticated, editorial design standard that commands respect from evaluators, clients, and hackathon judges.

---

## 2. Core Design Invariants & Standards

### Invariant 1: The Curated Institutional Color Palette
Every application must declare its visual tokens in CSS custom properties using a cohesive, nature-inspired palette:

```css
:root {
  /* Canvas Backgrounds */
  --canvas-bg: #fbfbf7;           /* Soft Ivory/Cream background */
  --canvas-surface: #ffffff;      /* Pure white card surface */
  --canvas-surface-subtle: #f5f6f0;/* Subtle tinted sage background */

  /* Typography Colors */
  --text-primary: #214239;        /* Deep Forest Green (Primary Headings) */
  --text-secondary: #55675f;      /* Soft Charcoal Sage (Body Text) */
  --text-muted: #789085;          /* Neutral Muted Sage (Captions, Labels) */

  /* Accent & Status Hues */
  --brand-emerald: #166c52;       /* Institutional Emerald (Primary Action) */
  --brand-emerald-hover: #12543f; /* Deep Emerald Hover */
  --status-amber: #d97706;        /* Warning / Offline State */
  --status-rose: #b91c1c;         /* High Risk / Critical Alert */
  --border-subtle: rgba(226, 230, 220, 0.95); /* Soft natural border */
}
```

### Invariant 2: Editorial Typography Standards
- **Headings & Brand Title:** Pair an authoritative, high-contrast serif font (e.g., `Newsreader`, `Fraunces`, or `Merriweather`) for titles and modal headers. This provides a human, bespoke, and authoritative feel.
- **Data Tables & Controls:** Use a clean, modern sans-serif (e.g., `Inter`, `Geist`, or `Outfit`) for numeric values, telemetry feeds, and table grids.
- **Monospace Cryptography:** Use `JetBrains Mono` or `Consolas` for hashes, nonces, and transaction signatures.

### Invariant 3: Layout Geometry & Sovereign Shell
- **Centered Floating Glass Card:** The app shell must be centered in a maximum width container (`max-width: 1440px; margin: 16px auto;`) with soft rounded corners (`border-radius: 16px`) and subtle elevation shadows (`0 8px 30px rgba(40, 54, 48, 0.05)`).
- **Harmonized Sidebar:** The navigation sidebar must match the palette of the main view (frosted white `rgba(255, 255, 255, 0.88)` with `backdrop-filter: blur(20px)`), never jet-black on a light canvas.
- **Independent Scrolling:** The content area and sidebar must scroll independently with slim, tinted 4px sage scrollbars.

### Invariant 4: Responsive Tri-Viewport Support
The interface must be tested and responsive across three breakpoints:
1. **Mobile (390px – 480px):** Single-column stack, drawer navigation, touch-friendly tap targets ($\ge 44\text{px}$).
2. **Tablet / Kiosk (768px – 1024px):** 2-column grid, compact KPI strip.
3. **Desktop (1200px – 1440px+):** Full 6-tab command center with multi-column layout.

### Invariant 5: Tactile Micro-Interactions
- Every button must have distinct `:hover`, `:active`, and `:disabled` styles.
- State transitions must use smooth CSS easing (`transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);`).
- Data loading states must display skeleton placeholders rather than empty blank white rectangles.

---

## 3. Generative Output: Synthesizing Design Specs

When invoked, this department generates the design specification chapter in `.project_docs/SPEC.md`:
1. **Color Token Palette & CSS Variables.**
2. **Typography Font Hierarchy & Google Fonts Import Links.**
3. **Component Design Standards** (Buttons, Cards, Badges, Modals, Tables, Forms).
4. **Layout Wireframe ASCII Diagrams.**
