# ACTION PROTOCOL: AUDIT & HEALTH CHECK
> **Action Type:** Diagnostic & Quality Assurance Operation  
> **Trigger:** Milestone completion, pre-deployment inspection, periodic health check, or post-incident review.  
> **Mandatory Invariant:** Exhaustive Multi-Tier Verification. Empirical Proof Capture. Zero Unresolved High-Severity Warnings.

---

## 1. The 6-Tier Comprehensive Audit Framework

A Sovereign Audit evaluates a project across five rigorous quality and security dimensions:

```
+---------------------------------------------------------------------------------------------------+
|                                  THE 6-TIER HEALTH AUDIT MATRIX                                   |
+--------------------+--------------------+--------------------+--------------------+---------------+
| TIER 1: CODEBASE   | TIER 2: SECURITY   | TIER 3: NETWORK    | TIER 4: UI/UX      | TIER 5: PERF  | TIER 6: WORKFLOW MAP |
| - TypeScript/Linter| - DAST / SAST scan | - DevTools inspect | - Layout viewport  | - Bundle size | - Madge circular map |
| - Unused imports   | - ArgosX / Strix   | - 4xx / 5xx audits | - WCAG AA contrast | - Cold-start  | - Code2Flow call graph|
| - Type assertions  | - Secret leaks     | - CORS / Headers   | - Anti-slop checks | - Memory leak | - AppMap runtime cfg |
+--------------------+--------------------+--------------------+--------------------+---------------+
```

---

## 2. Granular Step-by-Step Instructions

### TIER 1: Static Code Quality & Linter Audit
1. Execute the language linter and type checker:
   ```bash
   npm run build # TypeScript typecheck & bundling
   flutter analyze # Dart static analysis
   ```
2. Verify zero unhandled `any` types, zero dead imports, and zero circular dependencies.
3. Check for documentation integrity: Verify all exported functions and types have docstrings.

### TIER 2: Security & Vulnerability Audit (SAST & DAST)
1. **Secret Leakage Scan:**
   - Scan git history and working tree for hardcoded API keys, private Ed25519/RSA keys, or production passwords:
     - Search regex: `(sk_[live|test]|AIza[0-9A-Za-z-_]{35}|supabase.*service_role)`
   - Verify all credentials in `.env.example` are dummy placeholders.
2. **Dynamic Application Security Testing (DAST):**
   - Run the automated ArgosX/Strix verification test suite:
     ```bash
     npm run test:security
     ```
   - Assert that unauthenticated probes to sensitive data endpoints (`/persons`, `/cards`) return HTTP 401 or empty arrays.
3. **HTTP Edge Security Headers:**
   - Inspect production deployment headers via `curl -sI`:
     - `X-Content-Type-Options: nosniff`
     - `X-Frame-Options: DENY`
     - `Strict-Transport-Security: max-age=63072000`
     - `Content-Security-Policy: ...`

### TIER 3: Network Waterfall & DevTools Console Audit
1. Simulate a clean browser session launch.
2. Inspect network requests on initial page load:
   - **Zero Red Errors:** No requests returning 401, 404, or 500 on startup.
   - If an endpoint requires authentication, verify the client suppresses the probe until the user completes the login handshake.
3. Verify WebSocket / Realtime CDC connection health:
   - WebSocket connection stays open with heartbeat pings; handles automatic reconnection upon network drop.

### TIER 4: UI/UX, Design & Anti-AI Slop Audit
1. **Visual Theme Harmonization:**
   - Verify the interface adheres to a curated color palette (e.g. GovTech ivory `#fbfbf7` + forest green `#214239` + sage `#789085`).
   - Confirm sidebar and navigation cards do NOT clash jarringly with the background.
2. **Responsive Layout Stress Test:**
   - Inspect rendering across 3 viewport breakpoints:
     - Mobile Portrait (390px width).
     - Tablet / Edge Kiosk (768px width).
     - Desktop Command Center (1440px width).
   - Verify zero horizontal scrollbar overflow on mobile.
3. **Tactile Interaction Check:**
   - Check all interactive buttons for active/hover states, loading spinners, and disabled states during network requests.

### TIER 5: Performance, Bundle Size & Storage Audit
1. Inspect production bundle size:
   - Main JavaScript bundle should remain under target budget (warn if $>500$ KB uncompressed).
   - If a single component file exceeds 200 KB (e.g. monolithic `App.tsx`), recommend modularizing into discrete view components.
2. Inspect local storage engines:
   - Verify IndexedDB cursor queries are non-blocking.
   - Verify FIFO retention pruner caps active audit log entries to prevent browser storage exhaustion.

---

## 3. Mandatory Human Checkpoint Gate

At the conclusion of the 5-Tier Audit, the agent must output an **Executive Audit Report** and pause execution for human review:
```markdown
### 📋 Sovereign Audit Report Completed
- **Tier 1 (Codebase):** PASSED (0 linter errors, 0 type errors).
- **Tier 2 (Security):** PASSED (0 secret leaks, ArgosX test passing, RLS verified).
- **Tier 3 (Network):** PASSED (Zero 500s on startup, WebSockets stable).
- **Tier 4 (UI/UX):** PASSED (Responsive 390px–1440px, GovTech palette active).
- **Tier 5 (Performance):** PASSED (Dexie IndexedDB active, bundle within limits).
- **Recommendation:** Codebase is healthy and production-ready.
👉 **Awaiting human verification before deploying to live production.**
```


### TIER 6: Visual Workflow & Architectural Coupling Audit
1. **Execute Flowchart Synthesizer:**
   ```bash
   python SDK/tools/visualize_project_flow.py --project-dir .
   ```
2. **Circular Coupling Gate:**
   - Assert Madge reports zero circular dependencies: `[PASS] Zero Circular Dependencies Detected`.
   - If circular couplings are found, fail the audit immediately until decoupled.
3. **Concepts & Libraries Audit:**
   - Verify that all libraries in `package.json` are properly categorized and explained in `.project_docs/WORKFLOW_FLOWCHART.html`.
