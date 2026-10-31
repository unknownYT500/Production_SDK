---
name: context-engineering
description: Optimizes AI reasoning quality by actively managing context window saturation, token budgets, and working memory. Prevents hallucination, forgotten invariants, and truncated code. Use during complex refactoring, multi-file features, long-running agent sessions, or large codebases.
---

# Context Engineering & Memory Management Protocol

> **Objective:** Maintain peak AI reasoning capacity and eliminate memory degradation by actively budgeting tokens and pruning unnecessary context.

---

## When to Use This Skill
- Working on tasks that modify multiple large files or span many conversation turns.
- Noticing signs of context fatigue (abbreviated code outputs, forgotten rules, hallucinations).
- Structuring large refactoring plans or multi-agent execution waves.

---

## The 4 Rules of Context Engineering

### Rule 1: Search-First Discipline (Never Read Full Files Blindly)
- **Do NOT read entire 1,000-line files into working context** just to check a single function signature.
- **Always search first:**
  1. Use grep/ripgrep to locate the exact identifier or error line.
  2. Evaluate the match snippet.
  3. Perform a targeted slice read only on the specific line range needed (e.g., lines 45–80).

### Rule 2: The 250-Line / 3-File Wave Threshold
- If a proposed plan requires modifying more than 3 files or more than 250 lines of code, the AI must NOT attempt to execute it in a single prompt.
- The task must be partitioned into **Sequential Waves**:
  - **Wave 1:** Interface contracts, type declarations, schemas.
  - **Wave 2:** Storage engine, database models, migrations.
  - **Wave 3:** API routes, business services, controllers.
  - **Wave 4:** User interface components, views.
  - **Wave 5:** Verification suite, integration tests.

### Rule 3: Memory Compaction & Transcript Archiving
- When working in long sessions, persist summaries of completed phases directly into project files (e.g., `.project_docs/INCIDENT_LOG.md` or `ROADMAP.md`).
- This allows the agent to reference the compact file summary rather than re-reading hundreds of previous conversational messages.

### Rule 4: Subagent & Worktree Delegation
- For heavy, parallel tasks (e.g. running pentests, generating master PDF manuals, or heavy data processing), delegate work to isolated subagents or background tasks with their own scoped context.
- The parent orchestrator receives only the compact, verified exit status and output summary.
