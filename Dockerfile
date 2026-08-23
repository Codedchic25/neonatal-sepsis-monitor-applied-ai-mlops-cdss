# --- STAGE 1: COMPILING VIRTUAL ENVIRONMENT WITH UV DEPENDENCY MANAGER ---
FROM python:3.12-slim AS builder

WORKDIR /app

# Install native compilation requirements for standard C-extensions safely
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Inject the ultra-fast 'uv' binary tool inside the builder layer stage
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Establish safe container build parameters for deterministic optimization
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy project blueprint declarations to execute locked deterministic resolution
COPY pyproject.toml uv.lock ./

# Compile locked configurations directly into an isolated, independent virtual sandbox
RUN uv sync --frozen --no-cache --no-install-project

# --- STAGE 2: PRODUCTION RUNTIME MATRIX ENGINE ---
FROM python:3.12-slim AS runtime

WORKDIR /app

# Import the pre-compiled isolated virtual environment binaries from builder stage
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy verified clinical platform source folders and root layout configuration scripts
COPY app.py .
COPY src/ ./src/
COPY assets/ ./assets/

# Establish secure system environment default parameters aligned with production routing
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_CLIENT_SHOW_ERROR_DETAILS=true

# Expose the verified production-ready network streaming communications port
EXPOSE 8501

# Trigger the localized Streamlit presentation layout layer frame natively on port 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
