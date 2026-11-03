# ACTION PROTOCOL: CHANGING OR REFACTORING A FEATURE
> **Action Type:** Adaptive / Evolutionary Engineering Operation  
> **Trigger:** Requirements pivot, performance bottleneck, API redesign, technical debt reduction, or UX modernization.  
> **Mandatory Invariant:** Zero Breaking Changes to Active Consumers without Migration Paths. Contract Stability Guaranteed.

---

## 1. The 6-Stage Feature Refactoring Cycle

Modifying existing features carries the highest risk of collateral regressions. The AI agent must follow this 6-stage cycle:

```
[STAGE 1: BLAST RADIUS & IMPACT ANALYSIS] ──► Grep all callers, consumers, foreign keys & tests.
              │
              ▼
[STAGE 2: DEPRECATION & COMPATIBILITY] ──► Design backwards-compatible bridge or versioned route.
              │
              ▼
[STAGE 3: DATA & STATE MIGRATION PLAN] ──► Safe schema transformation without data loss.
              │
              ▼
[STAGE 4: SURGICAL ATOMIC EDIT] ──► Implement change cleanly; preserve existing comments & docs.
              │
              ▼
[STAGE 5: FULL REGRESSION TEST RUN] ──► Verify modified consumers AND unmodified legacy consumers.
              │
              ▼
[STAGE 6: DOCUMENTATION & SPEC SYNC] ──► Update architectural references, contracts & manuals.
```

---

## 2. Granular Step-by-Step Instructions

### STAGE 1: Blast Radius & Impact Analysis
1. **Automated Visual Dependency Check:**
   - Execute Madge to identify all module consumers:
     `node SDK/madge/bin/cli.js --extensions ts,tsx,js,jsx --json src`
   - Use Code2Flow to inspect upstream callers and downstream callee paths before touching signatures.
2. Before touching any file, search the entire codebase for all references to the function, class, table, or endpoint:
   - *Example:* Use ripgrep/grep to find all usages of `verifyEphemeralQrToken` or `activeTab`.
2. Map all dependencies:
   - Is this endpoint consumed by the Mobile app, Web app, or external webhooks?
   - If Mobile app consumes it, changing the response schema will break existing mobile devices!
3. If changing a database column, check for foreign key constraints, dependent views, and RPC triggers.

### STAGE 2: Deprecation & Backwards Compatibility Strategy
1. **The Parallel Run Principle:** If an API contract must change, introduce the new signature under a new version (`/api/v2/`) or accept both legacy and new parameter formats:
   ```typescript
   // Backwards-compatible parameter normalization
   const cardId = payload.cardId ?? payload.card_id ?? payload.cid;
   ```
2. Mark deprecated methods with `@deprecated` docstrings, specifying the replacement method and removal timeline.
3. Never suddenly delete fields from JSON responses; mark them optional or retain them during a transitional phase.

### STAGE 3: Data & State Migration Safeguard
1. **Never execute destructive table renames or drops directly.**
2. Follow the **Expand and Contract Pattern**:
   - **Step A (Expand):** Add the new column or table.
   - **Step B (Dual-Write / Backfill):** Update application to write to both old and new columns; backfill historical data.
   - **Step C (Read Switch):** Switch application reads to the new column.
   - **Step D (Contract):** Once verified across all platforms, drop the legacy column in a future maintenance migration.

### STAGE 4: Surgical Atomic Execution
1. Make targeted, surgical edits. Do NOT refactor unrelated code, reformat entire files, or delete existing developer comments.
2. Maintain documentation integrity: Preserve existing docstrings and inline comments.
3. Commit with atomic message: `refactor(<domain>): <concise explanation of change and rationale>`.

### STAGE 5: Full Regression Testing
1. Execute tests for the modified component.
2. Execute tests for **all dependent components identified in Stage 1**.
3. Verify client build compilation (`npm run build`, `flutter analyze`).

### STAGE 6: Architectural Specification & Visual Workflow Sync
1. Update `DATA_FLOWS.md` and `SPEC.md` to reflect the new behavior.
2. If UI was altered, update user manuals and judge demonstration guides.
3. **Regenerate Master Visual Flowchart:**
   `python SDK/tools/visualize_project_flow.py --project-dir .`
   - Verify that refactoring did not introduce circular dependencies (`madge --circular`).
   - Confirm updated call-graph paths in `.project_docs/WORKFLOW_FLOWCHART.html`.
