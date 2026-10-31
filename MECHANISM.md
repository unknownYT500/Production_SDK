# SOVEREIGN MASTER CONTROL MECHANISM (`MECHANISM.md`)
> **The Universal Enforcement Architecture Governing Autonomous AI Agents Across All Sessions & Projects**  
> **Status:** RATIFIED & ENFORCED  
> **Precedence:** Absolute. Overrides default model heuristics, conversational laziness, and context degradation.

---

## 1. Executive Summary & The Problem of Agent Drift

In long-running software engineering projects, AI agents inevitably suffer from **Agent Drift** and **Conversational Amnesia**:
1. **Context Compaction:** When conversations become long, LLMs lose previous instructions, leading to regression bugs, re-introducing old errors, or ignoring established conventions.
2. **Session Reset Amnesia:** A developer starts a new chat tab or switches to another laptop, and the agent acts like a generic, unconstrained chatbot with zero knowledge of the architecture.
3. **Model Nonchalance ("AI Slop"):** Under deadline pressure, models resort to placeholder comments (`// TODO: implement later`), mocked responses, fake proofs, or unverified claims.

`MECHANISM.md` is the **mechanical circuit breaker**. It guarantees that **every AI agent in every conversation on any project operates under the exact same strict, verified constitutional pipeline**.

---

## 2. The 4-Layer Defense-in-Depth Mechanism

To guarantee compliance without relying on human memory to re-prompt the AI, the Sovereign SDK implements **4 interlocking enforcement layers**:

```
+─────────────────────────────────────────────────────────────────────────────+
│ LAYER 1: ROOT SYSTEM INJECTION (AGENTS.md / GEMINI.md / CLAUDE.md)         │
│ Auto-injected into <user_rules> on EVERY TURN with supreme model priority.   │
+──────────────────────────────────────┬──────────────────────────────────────+
                                       │
                                       ▼
+─────────────────────────────────────────────────────────────────────────────+
│ LAYER 2: THE CONSTITUTIONAL LOCK (SDK/core_constitution/)                   │
│ - Zero-Lying & Empirical Proof Mandate                                       │
│ - Planning Lock: No code without .project_docs/SPEC.md & ROADMAP.md          │
│ - Context Budgeting: Max 250 LOC per atomic wave                             │
+──────────────────────────────────────┬──────────────────────────────────────+
                                       │
                                       ▼
+─────────────────────────────────────────────────────────────────────────────+
│ LAYER 3: ACTION PROTOCOL & ARCHITECT DISPATCH (SDK/action_protocols/)        │
│ Maps every user intent to a deterministic, step-by-step algorithm:          │
│ [Bug Fix 01] [Add Feature 02] [Refactor 03] [Revert 04] [Audit 05] [Input 06] │
+──────────────────────────────────────┬──────────────────────────────────────+
                                       │
                                       ▼
+─────────────────────────────────────────────────────────────────────────────+
│ LAYER 4: LIFECYCLE HOOK & FORENSIC RECORDER (.agents/hooks.json)            │
│ Executes python .agents/scripts/archive_conversation.py on "Stop" event.    │
│ Persists timestamped transcripts in .ai_transcripts/ for Git versioning.    │
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 3. The Mechanical Execution Circuit (The State Machine)

Every single AI response must strictly traverse the following 7-phase state machine:

```
[User Prompt Received]
        │
        ▼
[Phase 1: Intent Classification]
        │ ──► Is it a Bug Fix? ──────────► Action Protocol 01
        │ ──► Is it a New Feature? ──────► Action Protocol 02
        │ ──► Is it a Refactor/Change? ──► Action Protocol 03
        │ ──► Is it a Rollback/Revert? ──► Action Protocol 04
        │ ──► Is it a System Audit? ─────► Action Protocol 05
        │ ──► Is it User Feedback/Gate? ─► Action Protocol 06
        ▼
[Phase 2: Planning Lock Verification]
        │ Checks .project_docs/SPEC.md & ROADMAP.md
        │ If not finalized, BLOCK implementation and trigger Planning Phase.
        ▼
[Phase 3: Department Architect Consultation]
        │ Consults: Security (01), DB/RLS (02), UI/Design (03), Multi-Agent (04), Pentest (05)
        ▼
[Phase 4: Search-First Investigation]
        │ Prohibits blind whole-file reads. Uses ripgrep/grep to locate exact anchors.
        ▼
[Phase 5: Atomic Context-Budgeted Modification]
        │ Modifies code in discrete chunks (≤ 250 LOC). Preserves backward compatibility.
        ▼
[Phase 6: Empirical Verification Gate]
        │ MUST execute terminal command (curl, npm test, compiler, linter).
        │ Captures live stdout/stderr. NEVER accepts "it looks good".
        ▼
[Phase 7: Living Documentation & Archival]
        │ Appends incident/change to .project_docs/INCIDENT_LOG.md.
        │ On loop stop, Antigravity Hook archives session to .ai_transcripts/.
```

---

## 4. Cross-Platform Agent Enforcement Matrix

This mechanism is **model-agnostic** and functions across all major AI agent harnesses by linking to the universal discovery standards:

| Platform / IDE | Discovery Hook | Sovereign SDK Integration |
| :--- | :--- | :--- |
| **Google Antigravity IDE / CLI** | `AGENTS.md`, `GEMINI.md`, `.agents/rules/*.md` | Native `<user_rules>` injection. Discovers `.agents/skills/` and triggers `.agents/hooks.json`. |
| **Anthropic Claude Code** | `CLAUDE.md` | Create symlink: `CLAUDE.md -> AGENTS.md`. Auto-loaded into Claude system context. |
| **Cursor / Windsurf** | `.cursorrules`, `.windsurfrules` | Create symlink: `.cursorrules -> AGENTS.md`. Injected into model preamble. |
| **Aider / OpenCode / Codex** | `CONVENTIONS.md` or `AGENTS.md` | Directly reads `AGENTS.md` as repo-level instructions. |

---

## 5. Master Failsafe Rules (The Unbreakable Invariants)

If an agent attempts any of the following, it is in **direct constitutional violation**:

1. **The "Trust Me" Violation:** Claiming code works without executing a verification command and displaying actual terminal output.
2. **The "Silent Stub" Violation:** Leaving `TODO`, `pass`, or placeholder mocks in place of real logic without explicit user sign-off.
3. **The "Scope Creep" Violation:** Editing files unrelated to the user's explicit request or active roadmap wave.
4. **The "Blind File Read" Violation:** Calling full file views on multi-hundred line files without first using grep or targeted line slices.
5. **The "Doc Desynchronization" Violation:** Completing a bug fix or feature addition without appending an entry to `.project_docs/INCIDENT_LOG.md`.

---

## 6. How to Initialize Master Control in Any New Project

When bootstrapping any new software project:

```bash
# 1. Copy the SDK into your project
cp -r /path/to/SDK /path/to/new-project/SDK

# 2. Run the Autonomous Generator
python SDK/project_generator/generator_script.py --archetype web_fullstack --name "MyNewProduct" --target .
```

The generator guarantees that:
- `AGENTS.md` is placed at the workspace root pointing directly to this Master Control.
- `.project_docs/` (`SPEC.md`, `ROADMAP.md`, `INCIDENT_LOG.md`) is synthesized.
- `.agents/hooks.json` is active, binding `archive_conversation.py` to the `Stop` lifecycle event.
- All 14 specialized skills are installed into `.agents/skills/`.

**Peace of Mind Verified:** From the very first prompt in the new project, any AI agent will immediately read `AGENTS.md`, load the Supreme Constitution, respect the Planning Lock, and archive every conversation turn with timestamps.
