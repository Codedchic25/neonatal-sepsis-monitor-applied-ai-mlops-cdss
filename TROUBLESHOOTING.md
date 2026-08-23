# 🔧 TECHNICAL TROUBLESHOOTING GUIDE: SEPSIS MONITOR AI

This document provides immediate, step-by-step diagnostic procedures and resolution commands for networking conflicts, environment isolation issues, dependency failures, and runtime disruption within the platform pipeline.

---

## 🌐 1. Network & Port Allocation Conflicts

### 🚨 Symptom: `WinError 10054` or `ConnectionResetError` in Terminal
*   **Root Cause:** The networking subsystem forcefully dropped the connection. This occurs when a ghost background instance of Streamlit is locking the default port, or a corrupted parser triggers a script crash while the browser viewport is listening.
*   **Resolution:** Force-kill hanging background Python instances to release locked network sockets:
    ```powershell
    # On Windows (PowerShell)
    Stop-Process -Name "python" -Force

    # On macOS / Linux (Terminal)
    pkill -f python
    ```
    Alternatively, launch the server on an isolated alternative port:
    ```powershell
    uv run streamlit run app.py --server.port 8502
    ```

### 🚨 Symptom: Port 8501 is Already in Use
*   **Resolution:** Find the process ID (PID) binding the clinical viewport and terminate it safely:
    ```powershell
    # On Windows (PowerShell)
    netstat -ano | findstr :8501
    taskkill /PID <PID_NUMBER> /F

    # On macOS / Linux (Terminal)
    lsof -i :8501
    kill -9 <PID_NUMBER>
    ```

---

## 💻 2. Virtual Environment & Dependency Faults

### 🚨 Symptom: `ModuleNotFoundError: No module named 'reportlab'`
*   **Root Cause:** The library was installed globally on your machine instead of inside the isolated virtual environment (`.venv`) initialized by your workspace.
*   **Resolution:** Enforce absolute alignment by injecting the package directly via the target python environment wrapper:
    ```powershell
    uv pip install reportlab
    ```

### 🚨 Symptom: `No module named pip` Inside the Virtual Folder
*   **Resolution:** Inject and bootstrap core package management handlers back into the runtime matrix:
    ```powershell
    uv python -m ensurepip --default-pip
    uv pip install -r requirements.txt
    ```

---

## 💾 3. Database Layer Locks & Schema Corruption

### 🚨 Symptom: SQLAlchemy Operational Locks or `sqlite3.OperationalError`
*   **Root Cause:** The underlying database file schema was corrupted during abnormal script terminations, or concurrent threads generated a resource allocation lock.
*   **Resolution:**
    1. Terminate the active instance using `Ctrl + C`.
    2. Purge the stale database file directly from your root directory: `sepsis_v2.db`.
    3. Restart the platform; the app leverages its native schema instantiation layer to auto-generate a fresh, clean database matrix matching the active entity requirements.

---

## 🧠 4. AI Inference Gateway & XML Tag Parsing Errors

### 🚨 Symptom: `NameError` inside Output Functions or Collapsing Text Frames
*   **Root Cause:** The cloud LPU infrastructure returned an anomalous text payload that skipped mandated XML partitions (`<RAPORT>`, `<MEDICATIE>`), or the string slicing extraction layers hit a type mismatch.
*   **Resolution:** Ensure your string slicing functions index variables strictly as pure strings. Inspect the defensive fallback layer block (`except Exception as e:`). If network handshakes drop or a rate limit triggers, this block intercepts errors and gracefully streams hardcoded, deterministic local clinical protocols to prevent viewport crashes.

---

## 🎵 5. Multimedia Loops & PDF Sandbox Render Blockages

### 🚨 Symptom: Audio Stream Fails to Play or PDF Preview Remains Blank
*   **Root Cause:** The multimedia player cannot locate assets due to a broken path tree, or the embedded Base64 string contains syntax anomalies that trigger browser iframe blockades.
*   **Resolution:**
    *   Verify that the audio asset file exists at the explicit production path: **`assets/audio/womb_heartbeat.mp3`**.
    *   Ensure browser permissions allow media autoplay and looping parameters for `localhost:8501`.
    *   Run a strict syntax audit and formatting sweep with Ruff to ensure full codebase compliance before launching:
       ```powershell
       uv run ruff check --fix .
       uv run ruff format .
       ```
