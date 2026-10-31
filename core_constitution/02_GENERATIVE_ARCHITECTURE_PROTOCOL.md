# GENERATIVE ARCHITECTURE PROTOCOL
> **Status:** Constitutional Meta-Generation Protocol  
> **Purpose:** Establishes the autonomous mechanism whereby the pre-existing Department Architect `.md` files dynamically generate the customized, project-specific `.md` documentation suite required to plan, govern, and build the target product.

---

## 1. The Generative Architecture Concept

In traditional development, documentation is either completely missing or manually written as an afterthought.  
In the **Sovereign SDK**, the pre-existing Department Architect files act as **Generative Meta-Templates**:
- They contain the domain rules, invariants, validation rubrics, and structural patterns.
- When an AI agent initializes a new project or begins reverse-engineering an existing codebase, the **Main Supreme Architect** reads the project requirements, selects the relevant Department Architects, and executes the **Autonomous Document Synthesis Pipeline**.
- The output is a complete, synchronized suite of project-specific `.md` files that act as the active constitution and roadmap for that particular product.

```
+---------------------------------------------------------------------------------------------------+
|                            SOVEREIGN GENERATIVE ARCHITECTURE PIPELINE                             |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [INPUT REQUIREMENTS]                                                                             |
|  - Hackathon Rulebook / User Prompt / Client PRD                                                  |
|  - Existing Codebase Inspection (Reverse-Engineering)                                             |
|                                                                                                   |
|                                       │                                                           |
|                                       ▼                                                           |
|  [MAIN SUPREME ARCHITECT]                                                                         |
|  - Determines Project Archetype (Web, Mobile, Dual, Edge, API, AI)                                |
|  - Activates relevant Department Architects                                                       |
|                                                                                                   |
|                                       │                                                           |
|                 +─────────────────────┼─────────────────────+                                     |
|                 │                     │                     │                                     |
|                 ▼                     ▼                     ▼                                     |
|      [SECURITY ARCHITECT]    [DATABASE ARCHITECT]   [UI/UX ARCHITECT]                             |
|      - Extracts auth rules   - Designs tables & RPCs- Curates palette & tokens                    |
|      - Zero-trust invariants - Segregates telemetry - Selects typography                          |
|                                                                                                   |
|                                       │                                                           |
|                                       ▼                                                           |
|  [AUTONOMOUS SYNTHESIS OF PROJECT-SPECIFIC .MD FILES]                                             |
|  ├── .project_docs/                                                                               |
|  │   ├── SPEC.md                    # Core problem, user personas, non-negotiable requirements    |
|  │   ├── ROADMAP.md                 # Phase-by-phase execution waves and context budgets          |
|  │   ├── DATA_FLOWS.md              # Explicit system boundaries, protocols & packet lifecycles   |
|  │   ├── SECURITY_MATRIX.md         # Threat model, PII masking, RLS rules, and crypto schemes  |
|  │   ├── TEST_PLAN.md               # 20+ critical verification scenarios & negative tests        |
|  │   └── INCIDENT_LOG.md            # Living prompt-labeled troubleshooting journal               |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Mandatory Output Documents & Schemas

The Main Architect is required to synthesize the following six core documents before any implementation code is written:

### 1. `SPEC.md` (Product & System Specification)
- **Target Audience:** All team members, AI agents, and project evaluators.
- **Mandatory Sections:**
  1. Executive Summary & Problem Hook.
  2. Target User Personas & Real-World Constraints (e.g. 800M beneficiaries, offline FPS shops).
  3. Non-Negotiable Core Features (Phase 1 Prototype vs. Phase 2 Production).
  4. Explicit Exclusions & Out-of-Scope Boundaries.
  5. Regulatory & Compliance Grounding (e.g. NFSA 2013, DPDPA 2023, GDPR).

### 2. `ROADMAP.md` (Phased Wave Execution & Context Budgeting)
- **Target Audience:** Orchestrating AI agents and subagents.
- **Mandatory Sections:**
  1. Wave Execution Dependency Graph (Wave 1: Interfaces $\to$ Wave 2: Storage $\to$ Wave 3: UI $\to$ Wave 4: Integration).
  2. Task Decomposition Table with Line-Count & Complexity Budgets.
  3. Proof Requirements Matrix (exact verification artifact required per milestone).
  4. Human Inspection Checkpoints.

### 3. `DATA_FLOWS.md` (Boundary Contracts & Packet Lifecycles)
- **Target Audience:** Frontend, Mobile, Backend, and Database Engineers.
- **Mandatory Sections:**
  1. System Boundary Map & Accountability Matrix (explicit boundaries labeled 1 through N).
  2. Packet Lifecycles: ASCII diagrams showing the exact sequence of data packet transformations from client form to storage.
  3. Cryptographic Handshake & Nonce Protocols (hashing formulas, signature verification algorithms).
  4. Failure Modes & Recovery Protocols (offline collisions, cloning attacks, serverless reboots).

### 4. `SECURITY_MATRIX.md` (Zero-Trust Invariants)
- **Target Audience:** Security Lead, Penetration Testers (Strix / ArgosX).
- **Mandatory Sections:**
  1. Threat Model & Attack Vectors.
  2. Data Minimization & Field-Level Encryption Rules (e.g. AES-GCM-256 for PII).
  3. Row-Level Security (RLS) Policy Table (Role, Operation, Using clause, With Check clause).
  4. Cryptographic Key Management Lifecycle (Key generation, hardware keystore storage, rotation).

### 5. `TEST_PLAN.md` (Verification Scenarios & Negative Tests)
- **Target Audience:** QA Lead, Test Automation Runners (Vitest, Flutter Test).
- **Mandatory Sections:**
  1. Baseline Invariant Tests (ID uniqueness, canonical formatting, timestamp validity).
  2. Critical Positive Scenarios (Complete user journey execution).
  3. Critical Negative Scenarios (Replayed nonces, expired tokens, forged signatures, quota overdrafts, unauthorized role escalation).
  4. Performance & Resilience Benchmarks (Network blackout recovery, high-concurrency bursts).

### 6. `INCIDENT_LOG.md` (Living Troubleshooting & Audit Journal)
- **Target Audience:** Lead Developer, Post-Mortem Evaluators.
- **Mandatory Sections:**
  1. Chronological Incident Entries labeled with Prompt IDs and ISO timestamps.
  2. Root Cause Analysis (why the error happened at an architectural level).
  3. Permanent Failsafe Implementation (what rule was added to prevent recurrence).
  4. Verification Evidence (curl output, compiler log, test runner output).

---

## 3. The Generative Synthesis Rules

When synthesizing these documents, the Main Architect must adhere to these generative rules:
1. **No Boilerplate Filler:** Avoid vague generic advice (*"write clean code"*, *"implement good security"*). Every rule must specify concrete names, formulas, data types, and file paths.
2. **Mutual Consistency Guarantee:** The schema defined in `SECURITY_MATRIX.md` must match the tables in `DATA_FLOWS.md` and the test cases in `TEST_PLAN.md`. Any divergence is a constitutional violation.
3. **Planning Lock Invariant:** Code writing is strictly locked until the Main Architect outputs:
   `[STATUS: GENERATIVE ARCHITECTURE FINALIZED - PROCEED TO EXECUTION]`.
