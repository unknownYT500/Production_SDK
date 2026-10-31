---
name: retro
description: Conducts post-incident retrospectives and extracts architectural lessons to update project rules, preventing the AI agent and team from repeating past mistakes. Use after resolving critical bugs, overcoming technical roadblocks, completing milestones, or during post-mortems.
---

# Continuous Learning & Post-Incident Retrospective Protocol (`retro`)

> **Objective:** Systematically convert real-world development mistakes, production hurdles, and debugging sessions into permanent, version-controlled rules that govern future agent execution.

---

## When to Use This Skill
- Immediately after solving a difficult bug that took multiple attempts to fix.
- Following an emergency rollback or deployment failure.
- At the conclusion of a development sprint, hackathon phase, or release milestone.

---

## The 4-Step Retrospective Workflow

### Step 1: Timeline & Symptom Reconstruction
Document the chronological timeline of what happened:
- When was the issue introduced?
- What was the prompt or action that triggered it?
- What was the observed symptom (e.g., HTTP 500 on serverless edge, 401 on telemetry upsert)?

### Step 2: Extract the Root Cause Mechanism
Determine why the failure occurred at an architectural level:
- Did the failure stem from an overloaded table?
- Missing production environment variables?
- Serialization order differences between languages?
- Unauthenticated probing before login state was initialized?

### Step 3: Formulate the Battle-Tested Failsafe
Formulate a concrete, actionable rule that mechanically prevents this failure from ever recurring:
- *Bad Rule:* *"Be more careful with database migrations."* (Vague, unenforceable).
- *Good Rule:* *"Never overload a single table to store both telemetry and PII. Machine heartbeats must reside in a dedicated distribution_nodes table with separate RLS policies."* (Concrete, verifiable).

### Step 4: Persist the Rule to Living Project Constitution
Update the appropriate persistent project rulebook:
1. Append to `.project_docs/INCIDENT_LOG.md`.
2. Update the corresponding Department Architect file in `SDK/department_architects/`.
3. If universal, add the invariant to `SDK/core_constitution/00_SUPREME_CONSTITUTION.md`.
