---
name: grill-me
description: Proactively interviews the user with targeted Socratic questions to resolve ambiguous requirements, stress-test architectural decisions, and evaluate tradeoffs. Use when requirements are underspecified, multiple design paths exist, or design feedback is needed before coding.
---

# Socratic Requirement Alignment Protocol (`grill-me`)

> **Objective:** Eliminate misunderstandings and misaligned assumptions early by actively interviewing the stakeholder before building complex architectures.

---

## When to Use This Skill
- The user provides an open-ended or ambiguous request (e.g., *"add auth"*, *"make a dashboard"*, *"improve performance"*).
- Multiple architectural tradeoffs exist (e.g., SQLite vs. IndexedDB, JWT vs. Session cookies, Redis vs. In-Memory caching).
- Destructive or high-impact decisions must be evaluated before committing.

---

## The 4-Step Socratic Interview Workflow

### Step 1: Detect Underspecified Intent
Analyze the user's prompt against core architectural dimensions:
- **Authentication Model:** Is it multi-tenant RBAC, single-user admin, or anonymous kiosk?
- **Network Assumptions:** Must it operate offline, intermittently, or cloud-only?
- **Data Sensitivity:** Does the payload contain PII, financial data, or public telemetry?
- **Scale & Concurrency:** Single user vs. hundreds of concurrent transactions?

### Step 2: Formulate 2 to 4 Targeted Questions
Construct concise multiple-choice questions:
- Each question must address an architectural decision.
- Provide 2–3 viable, concrete options formatted as the user's direct response.
- Highlight the `(Recommended)` option based on the project's profile.
- Do NOT ask trivial yes/no questions; focus on trade-offs and domain constraints.

### Step 3: Present Questions Interactively
Present the questions clearly:
```markdown
### 🎯 Architectural Alignment Check
Before proceeding with implementation, please confirm your preferences for these key decisions:

1. **Storage & State Strategy:**
   - (A) Distributed Offline-First: Client-side storage (IndexedDB/SQLite) with background sync.
   - (B) Cloud-Centric: Direct database queries with optimistic UI caching.

2. **Security & Cryptographic Standard:**
   - (A) Zero-Trust Asymmetric: Ed25519 token signatures with client AES-GCM encryption.
   - (B) Standard Bearer JWT: HTTPS transport security with server-side validation.
```

### Step 4: Synthesize Decisions into Specifications
Once the user selects their preferred options, record the decisions immediately into the project's specification or architectural decisions log (`ADR.md`). Proceed with execution based on the agreed-upon constraints.

---

## Anti-Patterns Strictly Forbidden
- ❌ **Silent Assumptions:** Guessing what the user wants on critical architecture (e.g. assuming cloud-only when offline operation was needed).
- ❌ **Question Fatigue:** Asking 15 open-ended philosophical questions. Keep it to 2–4 high-impact multiple-choice questions.
- ❌ **Ignoring Answers:** Asking questions and then generating code that contradicts the user's chosen option.
