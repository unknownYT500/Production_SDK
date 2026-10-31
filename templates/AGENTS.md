# SOVEREIGN AGENT CONSTITUTION & MASTER CONTROL (`AGENTS.md`)
> **CRITICAL DIRECTIVE FOR ALL AI AGENTS:** You are operating under the **Sovereign AI Governance SDK**.  
> These instructions are **non-negotiable laws** with supreme priority over conversational heuristics or default model assumptions.

---

## 🏛️ Mandatory Governance & Architectural Invariants

### 1. The Supreme Constitution
Before taking any action, you must adhere to the core principles defined in:
- 📖 [**Supreme Constitution**](./SDK/core_constitution/00_SUPREME_CONSTITUTION.md)
- ⚙️ [**Master Control Mechanism**](./SDK/MECHANISM.md)

### 2. Zero-Lying & Empirical Proof Obligation
- **Never claim code works without execution proof.** You must execute terminal commands (test runners, compilers, linters, or curl requests) and show the exact stdout/stderr.
- **No Stubs or Mock Placeholders:** Never leave `// TODO`, `pass`, or mock data in place of production logic unless explicitly requested by the user.

### 3. Action Protocol Dispatch
Every user prompt must be mapped to and executed via its dedicated Action Protocol:
- **Bug Fixing:** Follow `SDK/action_protocols/01_ACTION_BUG_FIXING.md` (Isolate -> Reproduce -> Fix -> Regression Test).
- **New Feature:** Follow `SDK/action_protocols/02_ACTION_ADD_NEW_FEATURE.md` (Interface-first, context-budgeted wave progression).
- **Refactoring:** Follow `SDK/action_protocols/03_ACTION_CHANGE_OR_REFACTOR_FEATURE.md` (Blast radius analysis & backwards compatibility).
- **Rollback / Revert:** Follow `SDK/action_protocols/04_ACTION_REVERT_CHANGES.md` (Emergency git snapshot & atomic recovery).
- **Audit / Health Check:** Follow `SDK/action_protocols/05_ACTION_AUDIT_AND_HEALTH_CHECK.md` (5-tier comprehensive system inspection).
- **Human Review / Feedback:** Follow `SDK/action_protocols/06_ACTION_HUMAN_REVIEW_AND_INPUT.md` (Destructive stop-and-verify gates).

### 4. Department Architect Consultation
When making architectural decisions, align strictly with the specialized Department Architects in `SDK/department_architects/`:
- **Security & Zero-Trust:** Department 01 (Client AES-GCM-256, Ed25519 signing, PII masking).
- **Database & State:** Department 02 (Schema purity, granular RLS, atomic RPC mutations).
- **UI/UX & Anti-Slop:** Department 03 (Editorial GovTech palette, typography, micro-interactions).
- **Multi-Agent Sync:** Department 04 (Distributed domain locks, Git branch isolation).
- **Pentest & DAST:** Department 05 (DAST negative testing, security headers, Strix verification).
- **Living Logs & Archival:** Department 06 (Prompt-labeled logs, living docs, master PDF tech book).
- **Automation & Windows Safety:** Department 07 (Strict UTF-8 Windows safety, non-interactive scripts).

### 5. Search-First Discipline & Token Conservation
- **Never read entire large files blindly.** Always use ripgrep/grep first to locate relevant symbols, then inspect targeted line slices with `view_file`.
- Keep modifications atomic (≤ 250 LOC per wave) to prevent context pollution and hallucination.

### 6. Automated Conversation Archiving
- Every conversation turn is automatically recorded and archived with timestamps to `.ai_transcripts/` via the Antigravity `Stop` lifecycle hook.
- Do not disable or bypass `.agents/hooks.json`.
