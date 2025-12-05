from fastapi import Depends, FastAPI, HTTPException, status

from src.services.auth_service import AuthService, build_auth_dependency
from src.services.config_service import ConfigService
from src.services.logging_service import setup_logging
from src.utils.constants import APP_NAME, APP_VERSION

setup_logging()
config_service = ConfigService()
settings = config_service.load_yaml("settings.yaml")


def _build_auth_service() -> AuthService:
    auth_cfg = settings.get("auth", {})
    tenant_id = auth_cfg.get("tenant_id")
    client_id = auth_cfg.get("client_id")
    audience = auth_cfg.get("allowed_audience")
    authority = auth_cfg.get("authority")
    missing = [name for name, value in {"tenant_id": tenant_id, "client_id": client_id}.items() if not value]
    if missing:
        raise RuntimeError(f"Missing auth configuration values: {', '.join(missing)}")
    return AuthService(
        tenant_id=tenant_id,
        client_id=client_id,
        allowed_audience=audience or client_id,
        authority=authority,
    )


auth_service = _build_auth_service()
authz = build_auth_dependency(auth_service)
app = FastAPI(title=APP_NAME, version=APP_VERSION)


@app.get("/health")
def health() -> dict[str, str]:
    """Simple liveness check."""
    return {"status": "ok", "service": APP_NAME, "version": APP_VERSION}


@app.get("/me")
async def whoami(claims: dict = Depends(authz)) -> dict:
    """Return caller identity from Entra token."""
    return {
        "subject": claims.get("sub"),
        "name": claims.get("name"),
        "preferred_username": claims.get("preferred_username"),
        "aud": claims.get("aud"),
        "iss": claims.get("iss"),
    }
