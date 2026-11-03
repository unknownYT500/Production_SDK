# Sovereign AI Governance SDK (SovereignSDK)
> **The Constitutional Protocol & Meta-Architecture Governing Autonomous AI Engineering**  
> **Origin:** Born from real-world engineering trials, high-stress hackathon sprints, and independent penetration testing (ArgosX / Strix) of the **RationSafe / GrainTrust** sovereign public distribution platform.  
> **Mission:** To transform hard-earned engineering lessons and the 22 core points in [`SDK_POINTS.txt`](file:///c:/Users/shubh/Downloads/-hat--main/-hat--main/SDK/SDK_POINTS.txt) into an authoritative, modular governance framework. Every action, bug fix, feature addition, and refactor is governed by strict, self-moulding protocols that eliminate AI hallucination, error masking, multi-agent collisions, and AI-slop design.

---

## 🏛️ The Three-Tier Architecture

The Sovereign SDK is structured into three interlocking tiers of governance:

```
                                  +---------------------------------------+
                                  |         TIER 1: CORE CONSTITUTION     |
                                  |  - Zero-Lying & Harsh Factual Truth   |
                                  |  - Dynamic Project Profile Moulding   |
                                  |  - Generative Architecture Synthesis  |
                                  +-------------------+-------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  |     TIER 2: DEPARTMENT ARCHITECTS     |
                                  |  - Main Supreme Architect (Governor)  |
                                  |  - Security & Zero-Trust Architect    |
                                  |  - Database & Cloud State Architect   |
                                  |  - UI/UX & Anti-Slop Design Architect |
                                  |  - Multi-Agent Cross-Device Architect |
                                  |  - Pentest & Vulnerability Architect  |
                                  |  - Audit & Living Logs Architect      |
                                  |  - Automation & Scripts Architect     |
                                  +-------------------+-------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  |       TIER 3: ACTION PROTOCOLS        |
                                  |  - Action: Bug Fixing & Root Cause    |
                                  |  - Action: Addition of New Feature    |
                                  |  - Action: Changing / Refactoring     |
                                  |  - Action: Reverting / Failsafe Roll  |
                                  |  - Action: 5-Tier Health Audit        |
                                  |  - Action: Human Review & Intake      |
                                  +---------------------------------------+
```

---

## 📂 SDK Directory Map

```
SDK/
├── README.md                                         # This Master Architecture Document
├── SDK_POINTS.txt                                    # Historical 22 Core Post-Mortem Observations
├── raw_notes.md                                      # Developer hurdle staging journal
│
├── core_constitution/                                # Universal Invariants (All Projects)
│   ├── 00_SUPREME_CONSTITUTION.md                    # Zero-lying, proof-first, truth policy
│   ├── 01_PROJECT_PROFILE_AND_MOULDING_MATRIX.md     # Dynamic adaptation (Web, Mobile, Edge, API, AI)
│   └── 02_GENERATIVE_ARCHITECTURE_PROTOCOL.md        # Autonomous generation of .project_docs/
│
├── action_protocols/                                 # Protocols Governing Every Action
│   ├── 01_ACTION_BUG_FIXING.md                       # 6-step root-cause isolation & regression testing
│   ├── 02_ACTION_ADD_NEW_FEATURE.md                  # Interface-first, context-budgeted feature flow
│   ├── 03_ACTION_CHANGE_OR_REFACTOR_FEATURE.md       # Blast-radius analysis & backwards compatibility
│   ├── 04_ACTION_REVERT_CHANGES.md                   # 5-step emergency rollback & failsafe restoration
│   ├── 05_ACTION_AUDIT_AND_HEALTH_CHECK.md           # 5-tier multi-dimensional audit & human gate
│   └── 06_ACTION_HUMAN_REVIEW_AND_INPUT.md           # Deconstruction of feedback & destructive gates
│
├── department_architects/                            # The Specialized Governing Departments
│   ├── 00_MAIN_SUPREME_ARCHITECT.md                  # Master Governor: coordinates & spawns specs
│   ├── 01_SECURITY_AND_ZERO_TRUST_ARCHITECT.md       # AES-GCM-256 PII encryption & Ed25519 signing
│   ├── 02_DATABASE_AND_STATE_ARCHITECT.md            # Schema purity, RLS & atomic RPC mutations
│   ├── 03_UI_UX_AND_DESIGN_ARCHITECT.md              # Anti-slop, GovTech palette & typography
│   ├── 04_MULTI_AGENT_AND_SYNC_ARCHITECT.md          # Cross-device locks, PR reviews & Git queues
│   ├── 05_PENTEST_AND_VULNERABILITY_ARCHITECT.md     # Strix/ArgosX DAST, headers & threat models
│   ├── 06_AUDIT_REPORTING_AND_LOGS_ARCHITECT.md      # Prompt-labeled logs & PDF master tech book
│   ├── 07_AUTOMATION_AND_SCRIPTS_ARCHITECT.md        # UTF-8 Windows safety & non-interactive scripts
│   └── 08_WORKFLOW_AND_FLOWCHART_ARCHITECT.md       # Madge, Code2Flow & AppMap visual flowcharts
│
├── project_generator/                                # Autonomous Project Synthesis Engine
│   ├── generator_script.py                           # Python script to mould & bootstrap projects
│   └── archetypes/                                   # Project Archetypes (Dual, Web, Mobile, API)
│       ├── sovereign_dual.json                       # Sovereign Dual-Client (Web + Mobile Terminal)
│       ├── web_fullstack.json                        # Fullstack Web Application (React + Node + DB)
│       └── mobile_edge.json                          # Mobile Edge Terminal (Flutter + SQLite)
│
├── tools/                                            # Autonomous Utility Tools
│   ├── archive_conversation.py                       # Conversation archiver CLI & Antigravity Hook
│   └── visualize_project_flow.py                     # Master flowchart synthesizer (Madge + Code2Flow + AppMap)
│
├── madge/                                            # Bundled Module & Dependency Flowchart Engine
├── code2flow/                                        # Bundled Function Call-Graph Engine
├── appmap-js/                                        # Bundled Runtime Execution & API Tracing Engine
│
├── templates/                                        # Boilerplates for Initialized Projects
│   ├── hooks.json                                    # Antigravity Stop Lifecycle Hook configuration
│   └── scripts/
│       └── archive_conversation.py                   # Self-contained archiver script for .agents/scripts/
│
├── skills/                                           # Ready-to-Use Agent Skills Library (.agents/skills)
│   ├── spec-driven-development/                      # SDD: PRD & spec before code (Planning Lock)
│   ├── grill-me/                                     # Socratic requirements interview & tradeoff alignment
│   ├── test-driven-development/                      # Strict Red-Green-Refactor loop & test proof
│   ├── diagnosing-bugs/                              # Five Whys root cause analysis & anti-masking
│   ├── security-audit/                               # OWASP Top 10, secret scanning & DAST verification
│   ├── visual-workflow-mapping/                      # Interactive Madge + Code2Flow + AppMap visual flowcharts
│   ├── accidental-data-loss-prevention/              # Stop-and-Verify gate on destructive operations
│   ├── zero-downtime-migrations/                     # Expand-and-contract, schema purity & atomic RPCs
│   ├── frontend-design/                              # Anti-AI slop, curated palettes & editorial typography
│   ├── responsive-layout-builder/                    # Tri-breakpoint verification (390px, 768px, 1440px)
│   ├── context-engineering/                          # Token budgeting, search-first, memory compaction
│   ├── code-review/                                  # Senior engineer PR review before merge
│   ├── retro/                                        # Post-incident continuous learning & living rules
│   ├── cross-device-agent-sync/                      # Distributed domain locks & multi-laptop Git queues
│   └── pre-and-post-deploy-verify/                   # Pre-build checks & post-deploy live HTTP verification
│
└── SDK_development/                                  # Historical Laboratory & Incident Analysis
    ├── README.md                                     # Post-mortem methodology
    └── faults_and_failsafes_analysis.md              # Granular analysis of 7 critical hackathon hurdles
```

---

## ⏺️ Autonomous Build-Phase AI Conversation Archiving

One of the greatest dangers in AI pair programming is **conversational amnesia**—valuable architecture debates, prompt iterations, bug diagnoses, and decision rationale vanish once a session is closed or context-compacted.

The Sovereign SDK includes an **Autonomous Archiver Engine** powered by Antigravity Lifecycle Hooks:

1. **Zero-Friction Automation:**
   - Whenever an agent turn completes (`Stop` event), Antigravity executes `python ./.agents/scripts/archive_conversation.py --hook`.
   - The archiver reads the live Antigravity JSONL transcript and automatically saves a structured, human-readable Markdown log in `.ai_transcripts/` in your project folder:
     ```
     .ai_transcripts/conversation_<CONVERSATION_ID>_<TIMESTAMP>.md
     ```
2. **Lossless Forensic Trajectory:**
   - **User Prompts:** Chronologically cataloged with ISO UTC timestamps.
   - **Agent Responses:** Full architectural explanations, trade-off analyses, and reasoning.
   - **Tool Calls:** Collapsible `<details>` blocks capturing exact tool names, parameters, and statuses.
3. **Turnkey in Every Project:**
   - When you run `generator_script.py`, it automatically initializes `.agents/hooks.json`, `.agents/scripts/archive_conversation.py`, and `.ai_transcripts/` inside the target project.
4. **Manual Archiving On Demand:**
   - You can also archive any active session manually via CLI:
     ```bash
     python ./.agents/scripts/archive_conversation.py --conversation-id <CONV_ID>
     ```

---

## 🚀 Standalone Portability: Using the SDK in Future Projects

The `SDK/` folder is **100% project-independent** and can be dropped into any new repository (FinTech, SaaS, Mobile, GovTech, IoT, AI/ML):

1. **Copy the SDK:**
   ```bash
   cp -r /path/to/SDK /path/to/new-project/SDK
   ```
2. **Install the Agent Skills:**
   ```bash
   mkdir -p /path/to/new-project/.agents/skills
   cp -r /path/to/new-project/SDK/skills/* /path/to/new-project/.agents/skills/
   ```
3. **Bootstrap Project Documentation & Conversation Hooks:**
   ```bash
   python SDK/project_generator/generator_script.py --archetype web_fullstack --name "MyNewProduct" --target .
   ```
This activates the Supreme Governor, sets the Planning Lock, synthesizes the `.project_docs/` suite, sets up `.agents/hooks.json` for autonomous AI conversation archiving, and prepares your new project for production-grade engineering!

