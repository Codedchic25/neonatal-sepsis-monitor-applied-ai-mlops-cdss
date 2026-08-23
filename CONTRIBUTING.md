# 🚀 CONTRIBUTING GUIDELINES: SEPSIS MONITOR AI

Thank you for your interest in contributing to the **Sepsis Monitor AI Clinical Decision Support Platform**.

This document outlines the strict technical workflow required to propose new features, extend bio-mathematical algorithms, optimize telemetry pipelines, and contribute safely to this enterprise-grade platform.

---

## 🛠️ 1. Technical Environment Setup

All development must be executed inside an isolated virtual runtime to prevent dependency collisions or database connection locks.

### Step 1 — Fork and Clone the Repository
```bash
git clone https://github.com
cd sepsis-monitor-ai-cdss
```

### Step 2 — Initialize the Isolated Environment
The project leverages `uv` for ultra-fast, predictable dependency management. Run the following setup matrix:
```bash
# Initialize the virtual environment and activate it
uv venv
.venv\Scripts\activate  # On macOS/Linux use: source .venv/bin/activate

# Install core and development dependencies using uv execution layers
uv pip install -r requirements.txt
```

### Step 3 — Inject Infrastructure Environment Handles
```bash
cp .env.example .env
```
Populate the newly created `.env` file with your credentials (`GROQ_API_KEY`, `TWILIO_ACCOUNT_SID`, etc.).

---

## 📐 2. Engineering Architecture & Integration Rules

### A. Pharmacokinetic Engine & Dosing Logic
*   **Preserve Kinetic Integrity:** Do not alter the first-order biological exponential decay equations without peer-reviewed neonatal evidence.
*   **AKIShifting Scales:** Ensure any modification to metabolic clearance constants accounts for the +25% mild extension and -60% severe filtration collapse bounds based on the selected `Renal Function Status (AKI Tracker)` state.

### B. Viewport Persistence & Diskless Asset Streaming
*   **Session State Linkage:** Every interactive Streamlit widget, sidebar toggle, or audio element must lock onto a unique, explicit `st.session_state` key.
*   **In-Memory PDF Generation:** Clinical reports must never touch the local persistent file system. Stream all compiled ReportLab documents via encrypted binary streams.

---

## 🧪 3. Mandatory Testing & Quality Verification Matrix

This project follows a strict Test-Driven Development (TDD) cycle. No implementation branch will be merged until the entire automated audit pipeline returns a flawless green status.

### Phase 1 — Static Analysis & PEP 8 Compliance
```powershell
uv run ruff check --fix .
uv run ruff format .
```

### Phase 2 — Pytest Regression Execution
```powershell
uv run pytest -v
```
*All **22 core test scenarios** targeting the telemetry schema model must verify as **PASSED**.*

### Phase 3 — Promptfoo Adversarial Red-Teaming Audits
If your changes modify AI prompt construction, custom XML guardrails, or security boundaries, you must validate the safety evaluation matrix:
```bash
uv run promptfoo eval
```
*The automated safety evaluation framework must explicitly output:*
**Final Security Status Matrix: 100% IMMUNE (9/9 Advanced Scenarios Passed) 🛡️**
