---
name: spec-driven-development
description: Enforces writing an exhaustive, unambiguous Product and System Specification before writing implementation code. Use when starting a new project, adding a major capability, designing system architecture, or defining requirements before coding.
---

# Spec-Driven Development (SDD) Protocol

> **Objective:** Prevent architectural drift, scope creep, and unguided code generation by establishing an authoritative, versioned `SPEC.md` before any production source code is created or modified.

---

## When to Use This Skill
- Initializing any new project, microservice, mobile app, or client module.
- Adding a major feature, API endpoint, or data model.
- Transitioning a prototype into a production-grade system.
- Refactoring core business workflows or state machines.

---

## Non-Negotiable Invariant: The Planning Lock
**No implementation code (no `.ts`, `.tsx`, `.dart`, `.py`, `.sql`) may be created or edited until the specification document is written and its status is set to `FINALIZED`.**

---

## The 5-Step Specification Workflow

### Step 1: Discover & Extract Grounding Rules
Before writing the spec, extract the ground truth constraints:
1. Identify the core user personas and their operational constraints (e.g., offline connectivity, mobile battery, low bandwidth).
2. Identify statutory and regulatory bounds (e.g., data privacy laws, field encryption mandates, authentication requirements).
3. Document explicit exclusions: What is deliberately **out of scope** for this phase.

### Step 2: Define System Boundaries & Contracts
Explicitly define how data enters and exits the system:
- Input payloads with required fields and types.
- Output response models with status codes.
- Error code taxonomy (e.g., `ERR_101_VALIDATION`, `ERR_301_AUTH`, `ERR_500_INTERNAL`).
- External service boundaries (databases, third-party APIs, message queues).

### Step 3: Decompose into Phased Execution Waves
Break implementation into sequential waves where each wave produces verifiable proof:
- **Wave 1:** Interface contracts, domain models, and schemas.
- **Wave 2:** Storage engine, data access layer, and migrations.
- **Wave 3:** Business logic, state machines, and API endpoints.
- **Wave 4:** User interfaces and presentation layers.
- **Wave 5:** End-to-end integration tests and security verification.

### Step 4: Define Verification & Acceptance Criteria
For every feature in the spec, declare the exact empirical evidence required to prove completion:
- What automated test must pass?
- What command output or curl response must be captured?
- What negative error paths must be tested?

### Step 5: Finalize and Release the Planning Lock
Save the specification to `.project_docs/SPEC.md` or the project root.  
Set status banner: `Status: FINALIZED — PLANNING LOCK RELEASED`.

---

## Anti-Patterns Strictly Forbidden
- ❌ **"Just-in-time" Specs:** Writing a generic 3-line spec and immediately starting code.
- ❌ **Vague Acceptance Criteria:** Writing *"make it fast"* or *"ensure it's secure"* instead of concrete metrics (`p95 < 200ms`, `AES-GCM-256 for PII`).
- ❌ **Implementation Leaks:** Putting internal framework details in the functional specification rather than defining user outcomes and contracts.
