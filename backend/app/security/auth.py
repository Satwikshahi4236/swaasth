from typing import Optional
from jose import jwt
from jose.exceptions import JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import requests
from functools import lru_cache
from ..core.config import settings

http_bearer = HTTPBearer(auto_error=False)

class Auth0Error(HTTPException):
    pass

@lru_cache(maxsize=1)
def get_jwks() -> dict:
    if not settings.auth0_domain:
        return {"keys": []}
    jwks_url = f"https://{settings.auth0_domain}/.well-known/jwks.json"
    response = requests.get(jwks_url, timeout=5)
    response.raise_for_status()
    return response.json()


def verify_jwt(token: str) -> dict:
    if not settings.auth0_domain or not settings.auth0_audience:
        # In local/dev without Auth0 configured, accept unsigned tokens for ease of development
        try:
            return jwt.get_unverified_claims(token)
        except JWTError as exc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc

    unverified_header = jwt.get_unverified_header(token)
    jwks = get_jwks()
    rsa_key: Optional[dict] = None
    for key in jwks.get("keys", []):
        if key.get("kid") == unverified_header.get("kid"):
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
    if rsa_key is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token header")

    try:
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=settings.auth_algorithms,
            audience=settings.auth0_audience,
            issuer=f"https://{settings.auth0_domain}/",
        )
        return payload
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc


def get_current_user_claims(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)) -> dict:
    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return verify_jwt(credentials.credentials)