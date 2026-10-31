# DEPARTMENT ARCHITECT: AUTOMATION & SCRIPTS ARCHITECT
> **Department:** Department 07 — Automation Tooling & Cross-Platform Scripting  
> **Governed by:** Main Supreme Architect  
> **Mandatory Invariants:** Strict UTF-8 Encoding. Zero Interactive Prompts. Cross-Platform Windows/POSIX Compatibility.

---

## 1. Department Mission & Scope

The **Automation & Scripts Architect** maintains the project's operational tooling library. It ensures that scripts designed to automate builds, verify schemas, compile documentation, and synchronize repositories execute predictably across all developer operating systems (Windows PowerShell, macOS zsh, Linux bash).

---

## 2. Core Automation Invariants

### Invariant 1: Strict UTF-8 Windows Console Encoding
- **Learned Lesson:** On Windows, Python scripts often crash with `UnicodeEncodeError: 'charmap' codec can't encode characters` when printing emojis, checkmarks (`[PASS]`), or box-drawing characters because the default PowerShell console encoding is CP1252.
- **Mandate:** All Python automation scripts must explicitly configure UTF-8 encoding on standard I/O streams at startup:
  ```python
  import sys
  if sys.platform == 'win32':
      sys.stdout.reconfigure(encoding='utf-8')
      sys.stderr.reconfigure(encoding='utf-8')
  ```
- All file reads and writes must pass `encoding='utf-8'`:
  ```python
  with open(filepath, 'w', encoding='utf-8') as f:
      f.write(content)
  ```

### Invariant 2: Non-Interactive Automation Mandate
- Scripts executed by AI agents or CI runners must **never pause for interactive user input** (e.g. `input("Press Enter to continue")`).
- All scripts must accept CLI flags (`--yes`, `--non-interactive`, `--env production`) or default to safe automated modes.

### Invariant 3: Dual Shell Scripting Standard
- Core repository operations (validation, linting, syncing) must be provided in paired script formats:
  - `.sh` for Linux and macOS.
  - `.ps1` for Windows PowerShell.
- Both scripts must implement identical exit codes (`0` for success, non-zero for failure).

---

## 3. Reusable Script Library Standards

The department provides standard automation blueprints:
1. `validate-all.ps1` / `validate-all.sh`: Runs linting, typechecking, and tests.
2. `sync_repos.ps1`: Synchronizes shared schema files between companion web and mobile folders.
3. `generate_tech_book.py`: Automated headless Chrome/Edge PDF compiler.
4. `inspect_policies.py`: Automated Supabase RLS policy auditor.
