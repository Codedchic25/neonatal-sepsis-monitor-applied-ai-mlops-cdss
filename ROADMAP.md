# 🗺️ PRODUCT ROADMAP: SEPSIS MONITOR AI (Part 1)

This document outlines the strategic development phases, engineering milestones, and future integration paths for the Sepsis Monitor AI Clinical Decision Support Platform (CDSS).

---

## 🛑 Completed Milestones (Production Ready)

### 🎯 Milestone 1: Core Hybrid Telemetry & Architectural Foundation
*   **Stochastic Vector Simulation:** Implemented standard physiological baseline matrices (HR, Temp, SpO2, BP) with real-time stochastic shifting vectors.
*   **Pharmacokinetic Core v1:** Deployed first-order exponential decay models simulating biological clearance curves for high-acuity biomarkers (`crp` and `pct`).
*   **Pathological Shifting Scales:** Integrated stratified Renal Function Status (AKI Tracker) blocks, modulating biomarker half-lives dynamically (extending by 25% for Mild AKI or collapsing total clearance by 60% during Severe Anuria).
*   **Relational Persistence Framework:** Integrated thread-safe connection pooling engines mapped directly to a local SQLite embedded backend (`sepsis_v2.db`) for persistent hourly logging and automated session cleanups under the core database schema.

### 🎯 Milestone 2: Hybrid Cyber-Hardening, Customization & MLOps Automated Governance
*   **Synchronous Backend Regex Firewall:** Deployed a deterministic string-sanitization gateway inside `app.py` leveraging strict word boundaries to catch, strip, and substitute malicious prompt injection patterns (`IGNORE`, `OVERRIDE`) before LLM orchestration.
*   **Automated Continuous Integration:** Established an active GitHub Actions workflow (`.github/workflows/mlops.yml`) running structural linter analysis, `pytest -v` isolation suites, and live evaluation blocks on container runs.
*   **Promptfoo Red-Teaming Matrix Pass:** Completed the multi-language validation matrix securing a flawless **9/9 Advanced Scenarios Passed (100% Immune)** verdict against horizontal escalation, data harvesting, and prompt injection attempts.
*   **Granular Biometric Calculator:** Deployed a strict weight-driven mass tracking interface supporting operational thresholds from `0.50 kg` to `6.00 kg` that instantly calculates customized antibiotic regimes (Ampicillin 125.00 mg and Gentamicin 10.00 mg for a 2.50 kg preterm infant).
*   **In-Memory Diskless Documentation:** Integrated an on-the-fly binary ReportLab canvas flowable compiler that generates cryptographic clinical records directly in memory, bypassing storage caching leaks.

# 🗺️ PRODUCT ROADMAP: SEPSIS MONITOR AI (Part 2)

---

## 🔮 Future Development Horizons (Next Phases)

### 🚀 Milestone 3: Multi-Patient Telemetry Hub & Dynamic Access Isolation
*   **Centralized NICU Ward Overview:** Transition from single-infant tracking to a comprehensive grid array visualization matrix to monitor an entire active ward simultaneously.
*   **JWT-Based Authentication Suite:** Replace default role selection dropdowns with cryptographically hashed JSON Web Token (JWT) user access controls to separate Physician, Chief of Department, and Nurse clearance tiers.
*   **Asynchronous Alert Handling:** Decouple the local alert routing pipeline into an asynchronous event queue worker framework (Redis/Celery background threads) to eliminate presentation lag during high-frequency simulation steps.

### 🚀 Milestone 4: Interoperability Protocols & Edge Deployment
*   **HL7 FHIR Standard Integration:** Develop specialized data parsing adaptors to transform SQLite JSON telemetry metrics directly into official Fast Healthcare Interoperability Resources (FHIR) formatting for hospital EHR databases.
*   **Real-time WebSocket Streaming:** Port the discrete hourly simulation trigger into an automated, non-blocking asynchronous streaming socket layer pulling incubator vitals at 1Hz sub-second loops.

### 🚀 Milestone 5: Enhanced AI Intelligence & Local LLM Appliances
*   **Multi-Parametric Kinetic Forecasting:** Upgrade the bio-mathematical calculation engine to model dynamic biomarker fluctuations based on concurrent metabolic trends like Mean Arterial Pressure (MAP) shifts.
*   **Local LLM Deployment Trial:** Investigate transitioning the cloud-hosted Groq inference framework into a fully localized, quantized medical LLM model (e.g., Llama-3-Medical running on local GPU appliances) for offline enterprise functionality and complete data privacy.
