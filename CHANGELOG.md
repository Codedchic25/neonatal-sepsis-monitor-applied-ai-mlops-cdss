# 📝 Changelog: Sepsis Monitor AI (Part 1)

All notable changes to this project are documented in this file. This repository follows Semantic Versioning (`MAJOR.MINOR.PATCH`).

---

## — 2026-08-10

### ✨ Added
- **Synchronous Regex Gateway Firewall:** Engineered a hard-coded backend security validation layer using strict word boundaries `\b(IGNORE|OVERRIDE|CLEAN|SYSTEM RESET|DAN)\b` inside `app.py` to intercept and neutralize adversarial prompt injection vectors before API serialization.
- **Enterprise GitHub Actions Workflow:** Automated the MLOps pipeline infrastructure under `.github/workflows/mlops.yml` running lint checks, `pytest`, and automated red-teaming synchronously on isolated container environments.
- **Persistent Cyber Alert Architecture:** Integrated `st.session_state["cyber_alert_triggered"]` to ensure a permanent warning block renders on the clinician control board if a prompt hijacking is successfully blocked.

### 🐛 Fixed
- **Unreachable Dead Code Purge:** Cleaned logical anomalies and duplicate conditional branches inside `sanitize_clinical_payload` that caused unreachable code blocks.
- **Streamlit Reactive Rendering:** Integrated native `st.rerun()` gates inside the core database transactional control blocks (`Execute Telemetry Step` and `Simulate Injection Therapy`), fixing the graph latency issue and forcing instantaneous interface redraws.
- **Pytest Isolation Matrix Execution:** Expanded and verified the structural unit test blocks to guarantee 100% green compliance (**22 passed in 1.02s**).

# 📝 Changelog: Sepsis Monitor AI (Part 2)

---

## — 2026-08-09

### ✨ Added
- **Global Linting & Code Alignment:** Implemented complete repository-wide formatting and syntactic error resolution using the native `uv run ruff` execution layer.

### 🐛 Fixed
- **ORM Test Suite Synchronization:** Fully refactored `tests/test_models.py` to target the active `telemetry` SQL database schema definitions and integrated the isolated `db_session` fixture to resolve database default persistence constraints (`weight_kg` assertion bugs).
- **Hidden Character Cleansing:** Purged invalid non-breaking spaces (`\ua0` / `\u00a0`) and raw markdown tokens from python execution scripts that were causing compiler blockades within Pylance and Ruff.

---

## — 2026-08-04

### ✨ Added
- **Individualized Dosage Calculator:** Added weight-based dosage calculations for neonatal antibiotic decision support using the configured Ampicillin and Gentamicin protocol parameters.
- **Active Acoustic Loop Engine:** Added Streamlit audio playback for the local `womb_heartbeat.mp3` asset when Music Therapy is enabled.
- **In-Memory PDF Report Generation:** Added dynamic ReportLab PDF generation using `io.BytesIO`, incorporating patient profile, telemetry, biomarkers, and calculated medication information.
- **Embedded PDF Preview:** Added an embedded Base64 HTML iframe for in-app PDF preview with zoom, scrolling, and printing support.

## [v1.1.0] - Corecții de Siguranță Clinică și Extindere Teste
### Adăugat
- Implementat testul `test_guardrail_self_heals_missing_fcc_tag` pentru validarea auto-vindecării XML.
- Implementat testul `test_guardrail_intercepts_weight_relative_dosage_breach` pentru verificarea dozelor relative per kilogram corp (mg/kg).
- Numărul total de teste unitare verificate a crescut de la 22 la 24 (toate trecute cu succes).

### Modificat
- Optimizat `src/guardrails/guardrails.py` pentru a returna un tuplu și a suporta modificarea șirurilor imutabile.
- Corectat `src/services/ai_service.py` pentru a asigura rutarea corectă a telemetriei prin motorul RAG și prin Guardrails înainte de afișare.
