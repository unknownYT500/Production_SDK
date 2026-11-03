---
name: visual-workflow-mapping
description: Generates, updates, and verifies interactive visual workflow flowcharts, module dependency graphs, call graphs, and architectural models using Madge, Code2Flow, and AppMap. Use when starting a new project, adding major capabilities, refactoring architectures, onboarding to an AI-vibe-coded codebase, or preparing visual documentation for judges and human teammates.
---

# Visual Workflow Mapping Protocol (Madge + Code2Flow + AppMap)

> **Objective:** Prevent architectural drift, eliminate black-box AI code ("vibe coding amnesia"), and ensure the entire project workflow, call graph, and dependency structure is visually viewable, editable, and verifiable by the human team.

---

## When to Use This Skill
- Initializing any new project or hackathon build to map out starter architecture.
- After implementing or refactoring any feature that modifies $>2$ files or introduces a new library.
- When onboarding teammates or explaining code technicalities to judges.
- During system health checks to audit circular dependencies and call flow bottlenecks.

---

## The Three Core Tools Bundled in Sovereign SDK

1. **Madge (`SDK/madge/`)**:
   - Analyzes ES6/TypeScript/React/Node modules.
   - Detects all imports, exports, and circular dependencies.
   - Outputs JSON dependency trees and SVG graphs.
2. **Code2Flow (`SDK/code2flow/`)**:
   - Analyzes function definitions and control flow.
   - Generates algorithmic call graphs showing step-by-step logic.
   - Outputs DOT/SVG flowcharts.
3. **AppMap (`SDK/appmap-js/`)**:
   - Generates runtime trace configurations (`appmap.yml`).
   - Maps HTTP/REST routes and database interactions into sequence diagrams.

---

## The 4-Step Visual Workflow Execution

### Step 1: Automated Workflow Synthesis
Run the master synthesizer tool from the project root:
```bash
python SDK/tools/visualize_project_flow.py --project-dir .
```
This automatically:
- Scans `package.json` and catalogs all libraries and active design patterns.
- Runs `madge` across all `.ts`, `.tsx`, `.js`, `.jsx` files.
- Checks for circular dependencies.
- Runs `code2flow` across logic pipelines.
- Creates or updates `appmap.yml`.
- Compiles `.project_docs/WORKFLOW_FLOWCHART.html`.

### Step 2: Audit for Architectural Violations
Inspect the output report:
1. **Circular Coupling Check:**
   - If circular dependencies exist, they are listed with exact cycle paths (e.g. `A -> B -> A`).
   - **MANDATORY GATE:** You must refactor cyclic dependencies into unidirectional dependencies (e.g. extracting shared state into a pure model or store) before proceeding.
2. **Orphaned Modules:**
   - Detect files with 0 inward and 0 outward connections. Determine if they are dead code or missing integration.

### Step 3: Demystify AI Technicalities in `.project_docs/`
In the generated `.project_docs/WORKFLOW_FLOWCHART.html` and `.project_docs/SPEC.md`, verify that:
- Every newly introduced third-party library is accompanied by:
  - Exact package name and version.
  - Architectural rationale: What problem does it solve that existing code could not?
  - Data contract: How data enters and leaves the library.

### Step 4: Present Interactive Visual Flowchart to the User
Always surface the path to the newly compiled dashboard:
- Point the user to [WORKFLOW_FLOWCHART.html](file:///.project_docs/WORKFLOW_FLOWCHART.html).
- Provide a concise text summary of the workflow transitions, state changes, and module connections.

---

## Anti-Patterns Strictly Forbidden

- **Blind Vibe-Coding:** Writing $>300$ lines of code across multiple files without regenerating or verifying the visual workflow.
- **Ignoring Circular Warnings:** Dismissing circular dependency warnings reported by Madge as "harmless".
- **Undocumented Primitives:** Using complex libraries (e.g., tweetnacl, dexie, redis, zod) without adding their architectural explanation to the project concepts table.

