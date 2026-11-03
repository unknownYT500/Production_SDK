# DEPARTMENT ARCHITECT: WORKFLOW & FLOWCHART ARCHITECT
> **Department:** Department 08 — Workflow Visualization, System Comprehension & Anti-Blackbox Governance  
> **Governed by:** Main Supreme Architect  
> **Mandatory Invariants:** Mandatory Visual Workflow Flowchart. Zero Circular Dependencies. Full Technicality & Library Demystification.

---

## 1. Department Mission & Philosophy

When autonomous AI agents build ("vibe code") software under deadline pressure, human teams frequently lose track of:
1. **What code was created:** Hidden helper functions, obscure route handlers, or unintended side effects.
2. **What libraries and concepts were used:** Cryptographic signing, state machines, offline IndexedDB sync, or security headers introduced without team comprehension.
3. **How data actually flows:** Which frontend actions hit which backend endpoints, trigger which database RPCs, and alter which local storage states.

The **Workflow & Flowchart Architect** guarantees that **every project maintained by the Sovereign SDK remains 100% transparent, viewable, and editable through interactive visual flowcharts.** 

No AI agent is allowed to write code into a black box.

---

## 2. The Three-Engine Visual Toolchain

Department 08 integrates three production-ready industry visualizers bundled inside `SDK/`:

```
+─────────────────────────────────────────────────────────────────────────────+
|             DEPARTMENT 08: WORKFLOW & FLOWCHART ARCHITECT                   |
+──────────────────────────────────────┬──────────────────────────────────────+
                                       │
        +------------------------------+------------------------------+
        │                              │                              │
        ▼                              ▼                              ▼
+───────────────────────────+ +───────────────────────────+ +───────────────────────────+
|      ENGINE 1: MADGE      | |    ENGINE 2: CODE2FLOW    | |      ENGINE 3: APPMAP     |
| (Module & Dependency Flow)| | (Logic Call-Graph Engine) | | (Runtime Sequence Tracing)|
| - Maps imports & exports  | | - Maps function calls     | | - Maps HTTP/REST routes   |
| - Verifies zero circulars | | - Traces decision trees   | | - Traces DB mutations     |
| - Emits SVG & JSON graphs | | - Outputs DOT flowcharts  | | - Generates appmap.yml    |
+───────────────────────────+ +───────────────────────────+ +───────────────────────────+
                                       │
                                       ▼
+─────────────────────────────────────────────────────────────────────────────+
|  MASTER VISUAL DASHBOARD: .project_docs/WORKFLOW_FLOWCHART.html             |
|  - Standalone, interactive, zoomable, and viewable in any browser           |
|  - Categorizes all technical concepts, libraries, and architectural rules   |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 3. Core Constitutional Invariants Enforced by Department 08

### Invariant 1: Mandatory Visual Workflow Flowchart
- In every project governed by SovereignSDK, an interactive visual flowchart dashboard must reside at:
  ```
  .project_docs/WORKFLOW_FLOWCHART.html
  ```
- Any time a new feature is added, an API is changed, or a refactor is executed, the AI agent must invoke:
  ```bash
  python SDK/tools/visualize_project_flow.py --project-dir .
  ```
- The dashboard must be refreshed so human developers, judges, and teammates can inspect the live flowchart.

### Invariant 2: Zero Circular Coupling Mandate
- Spaghetti architecture and tangled circular dependencies are strictly forbidden.
- The Madge dependency engine must report `Zero Circular Dependencies`.
- If a cycle is detected (e.g. `App.tsx -> storage.ts -> App.tsx`), the build is **BLOCKED** and marked `FAIL_CIRCULAR_COUPLING` until refactored into a unidirectional data flow.

### Invariant 3: Complete Technicality & Concept Disclosure
- Autonomous agents must never import a package or use a complex design pattern without explaining it.
- In `WORKFLOW_FLOWCHART.html` and `.project_docs/SPEC.md`, every library must have:
  1. Exact package name and version.
  2. The specific architectural problem it solves.
  3. How data flows into and out of that library.

### Invariant 4: Call-Graph Logic Traceability
- Complex multi-step operations (such as offline voucher generation, biometric verification, or payment reconciliation) must have their internal algorithmic branches rendered via `code2flow`.
- Reviewers must be able to view:
  ```
  [User Action] ──► [Input Validation] ──► [Cryptographic Sign] ──► [Optimistic UI] ──► [Background Sync]
  ```

---

## 4. Operational Execution Trigger

Whenever a hackathon theme or new project brief is given to Antigravity:
1. **Intake Phase:** Supreme Architect moulds project profile.
2. **Scaffold Phase:** Department 08 verifies `appmap.yml` and initial workflow contracts.
3. **Verification Wave:** After every code phase, Department 08 compiles `.project_docs/WORKFLOW_FLOWCHART.html`.
4. **Team Sync Gate:** Before raising pull requests or syncing with teammate machines, the updated flowchart is reviewed to prevent colliding architecture.

