import time
from typing import Any, Dict, Optional

import httpx
import jwt
from fastapi import Header, HTTPException, status


class AuthService:
    """Simple Entra ID JWT validator using JWKS discovery."""

    def __init__(self, tenant_id: str, client_id: str, allowed_audience: str, authority: str) -> None:
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.allowed_audience = allowed_audience or client_id
        self.authority = authority.rstrip("/")
        self._jwks_cache: dict[str, Any] = {}
        self._jwks_cached_at: float = 0.0
        self._jwks_ttl = 60 * 60  # 1 hour

    async def _get_jwks(self) -> Dict[str, Any]:
        now = time.time()
        if self._jwks_cache and now - self._jwks_cached_at < self._jwks_ttl:
            return self._jwks_cache
        jwks_uri = f"{self.authority}/discovery/v2.0/keys"
        async with httpx.AsyncClient() as client:
            resp = await client.get(jwks_uri, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            self._jwks_cache = {key["kid"]: key for key in data.get("keys", [])}
            self._jwks_cached_at = now
            return self._jwks_cache

    async def _get_signing_key(self, kid: str) -> Dict[str, Any]:
        jwks = await self._get_jwks()
        if kid not in jwks:
            self._jwks_cache = {}
            jwks = await self._get_jwks()
        key = jwks.get(kid)
        if not key:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unknown signing key")
        return key

    async def verify_bearer(self, authorization: Optional[str]) -> Dict[str, Any]:
        if not authorization or not authorization.lower().startswith("bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")
        token = authorization.split(" ", 1)[1]
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")
        key = await self._get_signing_key(kid)
        try:
            payload = jwt.decode(
                token,
                key=jwt.algorithms.RSAAlgorithm.from_jwk(key),
                audience=self.allowed_audience,
                issuer=f"{self.authority}/{self.tenant_id}/v2.0",
                algorithms=["RS256"],
                options={"verify_at_hash": False},
            )
        except jwt.PyJWTError as exc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc
        return payload


def build_auth_dependency(auth_service: AuthService):
    async def _authorize(authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
        return await auth_service.verify_bearer(authorization)

    return _authorize