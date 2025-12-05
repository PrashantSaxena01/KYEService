# KYEService

Multi-agent service skeleton with FastAPI entrypoint, agent registry, and orchestration hooks.

## Quick start (Python 3.13.1)
1. Create a virtual environment and install dependencies:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and set Azure values:
   - `AZURE_AD_TENANT_ID`, `AZURE_AD_CLIENT_ID`, `AZURE_AD_ALLOWED_AUDIENCE`
   - `AZURE_AI_SEARCH_ENDPOINT`, `AZURE_AI_SEARCH_KEY`, and per-agent index names
3. Run the API locally:
   ```powershell
   uvicorn src.api.fastapi_app:app --reload
   ```
4. Call the protected endpoint with a valid Entra bearer token:
   ```bash
   curl -H "Authorization: Bearer <token>" http://localhost:8000/me
   ```

## Project layout
- `configs/`: YAML configs for agents, orchestrations, and settings.
- `src/api/`: FastAPI app entrypoint.
- `src/agents/`: Agent implementations, tools, and workflows.
- `src/orchestrations/`: Multi-agent orchestration logic and routing.
- `src/services/`: Shared services like config, logging, search, vector store, telemetry.
- `src/utils/`: Helpers and constants.
- `tests/`: Test skeletons organized by domain.

## Development notes
- Target runtime: Python 3.13.1.
- Authentication: Entra ID JWT validation via `/me` route; health remains open.
- Search: Azure AI Search per-agent indexes configured in `configs/settings.yaml` and `.env`.
- Microsoft Foundry (Azure AI Foundry) models can be integrated via Azure SDKs as needed.
- Ruff/pytest hooks can be added later; see `pyproject.toml` for starter config.
