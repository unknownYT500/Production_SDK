# DEPARTMENT ARCHITECT: AUDIT, REPORTING & LIVING LOGS ARCHITECT
> **Department:** Department 06 — Documentation Engineering & Living Forensic Logs  
> **Governed by:** Main Supreme Architect  
> **Mandatory Invariants:** Prompt-Labeled Incident Logging. Continuous Living Specs. Publication-Grade PDF Master Tech Book.

---

## 1. Department Mission & Philosophy

The **Audit, Reporting & Living Logs Architect** ensures that engineering decisions, bug fixes, and system architectures are never lost to conversational amnesia. It enforces a culture of **Living Documentation**:
- Writing code without updating documentation is treated as an incomplete task.
- Every major incident or bug fix is recorded with its triggering prompt label and root cause.
- Technical specifications, data flow diagrams, and judge explanation guides are maintained continuously in Markdown and can be compiled into publication-grade PDF volumes on demand.

---

## 2. Core Living Documentation Invariants

### Invariant 1: Prompt-Labeled Incident Journaling
Every bug fix, architectural refactor, and security patch must be appended to `.project_docs/INCIDENT_LOG.md`.  
Each entry must contain:
1. **Timestamp:** ISO-8601 string (`YYYY-MM-DDTHH:MM:SS+05:30`).
2. **Triggering Prompt Label:** The exact prompt ID or user instruction that initiated the action (e.g. `PROMPT-REF-20261031-09`).
3. **Component Affected:** Relative file paths (e.g., `web/src/api/security.ts`).
4. **Observed Symptom:** Exact error message or failing behavior.
5. **Root Cause Analysis (RCA):** Deep architectural explanation.
6. **Applied Engineering Fix:** Exact technical changes made.
7. **Verification Proof:** Command output, test runner log, or screenshot evidence.
8. **Permanent Failsafe Added:** The new rule or assertion added to prevent future recurrence.

### Invariant 2: Publication-Grade PDF Master Tech Book
- Documentation must not remain trapped in plain text.
- The project maintains an automated Python script (e.g. [`generate_tech_book.py`](file:///c:/Users/shubh/Downloads/-hat--main/-hat--main/scripts/generate_tech_book.py)) that:
  1. Parses all Markdown files using `markdown` with Pygments syntax highlighting (`github-dark` theme).
  2. Injects modern typography (`Inter` for prose, `JetBrains Mono` for code, `Newsreader` for headers).
  3. Uses headless Google Chrome or Microsoft Edge (`--headless --print-to-pdf`) to render pixel-perfect A4 PDF pages with running headers, footers, and page numbers.
  4. Merges individual chapters into an authoritative master engineering book (e.g. `Giant_Tech_Book.pdf`) using `pypdf`.

### Invariant 3: Markdown Hyperlink Integrity
- All file references in Markdown documents must use valid clickable links:
  - Format: `[filename](file:///absolute/path/to/file)`.
  - Line range format: `[filename#L10-L25](file:///path/to/file#L10-L25)`.
- Never enclose URLs in backticks inside the link syntax.

### Invariant 4: Autonomous Build-Phase AI Conversation Trajectory Archiving
- Every project in its active build or maintenance phase must archive all interactions with AI agents directly within the project repository under `.ai_transcripts/`.
- **Lifecycle Hook Trigger:** Configured via `.agents/hooks.json` listening to the Antigravity `Stop` lifecycle event, automatically executing `python ./.agents/scripts/archive_conversation.py --hook`.
- **Output Contract:** Generates timestamped, readable Markdown files (`.ai_transcripts/conversation_<conv_id>_<timestamp>.md`).
- **Data Captured:**
  1. Full chronological user prompts with exact timestamps and turn indexes.
  2. Agent architectural reasoning, diff proposals, and responses.
  3. Collapsible records of every tool call, parameter dictionary, and return status.
- **Git Retention:** Trajectory logs are version-controlled alongside source code, providing an immutable audit trail of prompt engineering, architectural tradeoffs, and debugging sessions.

---

## 3. Generative Output: Synthesizing Living Documentation

When invoked, this department generates:
1. `.project_docs/INCIDENT_LOG.md` pre-seeded with project initialization entries.
2. `.agents/hooks.json` configured with the autonomous conversation archiver hook.
3. `.agents/scripts/archive_conversation.py` for headless hook execution and CLI archiving.
4. `.ai_transcripts/` directory for continuous build-phase trajectory preservation.
5. The standalone judge and architecture manuals (`web_explained/`, `app_explained/`).
6. Automated PDF compilation scripts in `scripts/`.
