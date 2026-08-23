# ❓ Clinical & Technical FAQ: Sepsis Monitor AI (Part 1)

This document answers the most frequently asked technical and operational questions regarding the synchronization of biometric mass calculation, background media streaming, database triggers, and real-time PDF previewing within the platform.

---

### Q1: Why does the Music Therapy audio player keep playing and not reset when I click "Execute Telemetry Step"?
*   **Answer**: This behavior is intentional and driven by our **Dynamic Key Persistence Engine**. The sidebar dropdown selector (`Music Therapy Status`) is bound to an explicit widget token within `st.session_state`. This approach completely insulates the UI state from the reactive page-refresh cycle of Streamlit. As a result, the low-frequency neurodevelopmental intrauterine audio file (**`womb_heartbeat.mp3`**) continues to play acoustically in a continuous loop (`loop=True`) across simulation hours without track clipping, lag, or resetting.

### Q2: How does the app ensure that no unencrypted patient data leaks onto the server's hard drive during PDF export?
*   **Answer**: The document compilation architecture is completely **diskless and in-memory**. When a report generation is requested, the ReportLab engine writes the dynamic flowable tables directly into a binary memory buffer (`io.BytesIO()`). The system serializes this binary data on-the-fly into a clean Base64-encoded text string and streams it into a sandboxed download trigger button. At no point is an unencrypted PDF file written to the physical storage disk of the server host.

### Q3: Why do the antibiotic dosages in the card views shift immediately when I change the newborn's weight?
*   **Answer**: The application includes a strict, reactive **Biometric Mass Calculator** tied to core institutional NICU protocols. The numerical `Infant Weight (kg)` widget updates the session state variable in real time. This change instantly triggers an automatic recalculation of the medication limits ($100\text{ mg/kg/day}$ divided every 12h for Ampicillin split-infusions and $4\text{ mg/kg/day}$ for single daily Gentamicin hits). The values scale down to the exact micro-milligram (rendering exactly `125.00 mg` and `10.00 mg` respectively for a `2.50 kg` infant) to prevent dangerous human dosing errors during shifts.

# ❓ Clinical & Technical FAQ: Sepsis Monitor AI (Part 2)

---

### Q4: What happens to the system's analytical capabilities if the external Groq Cloud LPU framework suffers a network dropout?
*   **Answer**: The system integrates an automated **Fail-Safe Local Determinism Framework**. All remote client completions are encapsulated inside robust exception catch blocks. If a timeout or API authentication failure is detected, the system immediately aborts the active cloud inference pipeline and falls back onto local, hardcoded medical protocols. This approach guarantees that the local SQLite logging, line chart compilation, active audio streams, localized console background notifications, and ReportLab PDF download panels continue running completely offline without freezing the clinical UI viewport.


### Q5: How do I completely erase a patient's historical telemetry trends at the end of my clinical shift?
*   **Answer**: To close out an active cycle and ensure strict data minimization, click the red **"Clinical Reset System"** button located in the central dashboard action layout. This command triggers a transactional database truncate sequence (`DELETE FROM telemetry`) targeting the local SQLite architecture. It deletes all historical records from the relational tables, resets active biomarker tracking to normal patient baseline constants (**`CRP = 5.0 mg/L`**, **`PCT = 0.5 ng/mL`**), clears the line chart viewport, and displays successful confirmation toasts and alerts reading *"System Reset Complete."* for the next patient admission.

### Q6: How does the system resolve schema-to-model mismatches dynamically if the SQLite database requires columns unmapped in the core SQLAlchemy model?
*   **Answer**: The platform implements a non-intrusive **Runtime Model Extension & Constructor Patching Pattern** directly within the application initialization layer. When a local database migration introduces a mandatory non-nullable constraint that is missing from the compiled class attributes, standard instance creation throws a `TypeError`. The system dynamically fixes this by injecting a `column_property` directly into the class namespace at runtime. It then wraps the native declarative constructor with a `patched_init` hook that intercepts keyword arguments, binds the tracking strings securely to the instance's underlying `__dict__`, and guarantees that the SQLAlchemy flush compiler submits fully compliant SQL statements to SQLite without requiring direct schema refactoring or causing service dropouts.

### Q7: How does the server-side Regex Firewall mitigate Prompt Injection risks differently from simple system prompt constraints?
*   **Answer**: While system prompts act as soft instructions that models can sometimes be coerced to ignore via jailbreaks, our **Synchronous Regex Gateway Firewall** acts as a hard filter inside the application backend layer (`app.py`). It intercepts inputs before they ever reach the Groq API. It scans all string inputs for critical adversarial command tokens using word boundaries (`\b(IGNORE|OVERRIDE|CLEAN|SYSTEM RESET|DAN)\b`). If a match is found, it immediately stops the malicious command block, substitutes the phrases with safe markers, saves the flag in `st.session_state` to render a persistent alert block in the interface, and enforces absolute grounding, preventing prompt hijacking or token resource exhaustion.
