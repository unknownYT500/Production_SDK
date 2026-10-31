# ACTION PROTOCOL: HUMAN REPORT, REVIEW & FEEDBACK INTAKE
> **Action Type:** Collaborative Alignment & Governance Operation  
> **Trigger:** User feedback, judge evaluation comments, code review notes, UI criticism, or stakeholder feature requests.  
> **Mandatory Invariant:** Active Listening. No Defensive Hallucination. Structured Task Decomposition. Stop-and-Verify on Destructive Actions.

---

## 1. The 5-Stage Human Feedback Intake Cycle

When receiving human input—especially critical feedback or subjective review comments—the AI agent must process it through this structured intake cycle:

```
[STAGE 1: FEEDBACK DECONSTRUCTION] ──► Parse unstructured human input into categorized issues.
              │
              ▼
[STAGE 2: CLARIFICATION & ALIGNMENT] ──► Clarify ambiguity; present design options if subjective.
              │
              ▼
[STAGE 3: ACTION PLAN DECOMPOSITION] ──► Map feedback to specific file paths, tasks & proof targets.
              │
              ▼
[STAGE 4: DESTRUCTIVE STOP GATE] ──► Obtain explicit confirmation before irreversible operations.
              │
              ▼
[STAGE 5: EXECUTE & EVIDENCE DELIVERY] ──► Implement changes; deliver before-and-after proof.
```

---

## 2. Granular Step-by-Step Instructions

### STAGE 1: Feedback Deconstruction & Categorization
1. Never respond defensively or brush off user critique (*"Actually, the black sidebar was intended..."*).
2. Deconstruct the user's input into four standard categories:
   - **Category A: Aesthetic & UI/UX** (e.g., *"the sidebar looks haphazard"*, *"black color does not fit"*).
   - **Category B: Functional Bug** (e.g., *"clicking approve throws a 401 error"*).
   - **Category C: Security / Policy Mandate** (e.g., *"don't expose citizen phone numbers"*).
   - **Category D: Architectural Pivot** (e.g., *"switch from cloud-only to offline-first"*).

### STAGE 2: Clarification & Alignment
1. If the feedback is subjective (e.g., *"make it look more presentable"*):
   - Formulate 2–3 concrete design options based on established design principles (e.g., Option 1: Frosted white GovTech card; Option 2: Sage minimalism).
   - Recommend the option that best fits the existing project identity.
2. If the user asks for a feature that violates a core invariant (e.g. disabling encryption or storing passwords in plaintext):
   - Respectfully explain the security risk: *"Disabling AES-GCM encryption will expose citizen PII to unauthenticated scraping and fail the ArgosX penetration test. Can we instead implement an automated local decryption layer?"*

### STAGE 3: Action Plan Decomposition
1. Convert the feedback into a concrete, numbered task list:
   - Identify the exact target files (e.g., `web/src/client/index.css`, `web/src/client/App.tsx`).
   - Define the exact CSS variables, functions, or schemas being adjusted.
   - Set the required verification evidence (e.g. headless build compilation, before/after screenshot).

### STAGE 4: The Destructive Stop Gate
The agent is **strictly prohibited** from performing any of the following without explicit, written confirmation:
- Dropping or truncating database tables or schemas.
- Deleting user data or clearing cloud storage buckets.
- Upgrading major framework versions (e.g. React 18 $\to$ 19, Flutter 2 $\to$ 3) that could break dependencies.
- Overwriting large existing specification files.

### STAGE 5: Execution & Evidence Delivery
1. Implement the requested adjustments in accordance with the appropriate Action Protocol (`BUG_FIXING` or `CHANGE_FEATURE`).
2. Present the user with a concise summary linking to the modified files, accompanied by the required proof artifact.
3. Update the project's living documentation (`INCIDENT_LOG.md` or user manual).
