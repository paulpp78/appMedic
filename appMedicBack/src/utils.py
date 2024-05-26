import json
from functools import wraps
from typing import Dict
from urllib.request import urlopen

from flask import request, jsonify, g
from jose import jwt

from config import Config


class AuthError(Exception):
    def __init__(self, error: Dict[str, str], status_code: int):
        super().__init__()
        self.error = error
        self.status_code = status_code


def get_token_auth_header() -> str:
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected",
            },
            401,
        )

    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must start with Bearer",
            },
            401,
        )
    elif len(parts) == 1:
        raise AuthError(
            {"code": "invalid_header", "description": "Token not found"}, 401
        )
    elif len(parts) > 2:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must be Bearer token",
            },
            401,
        )

    return parts[1]


def requires_permission(required_permission: str):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = get_token_auth_header()
            unverified_claims = jwt.get_unverified_claims(token)
            if unverified_claims.get("permissions"):
                token_permissions = unverified_claims["permissions"]
                if required_permission in token_permissions:
                    return f(*args, **kwargs)
            return (
                jsonify(
                    {
                        "error": "insufficient_permission",
                        "error_description": "The request requires higher privileges than provided by the access token.",
                    }
                ),
                403,
            )

        return decorated_function

    return decorator


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen(f"https://{Config.AUTH0_DOMAIN}/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"],
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=Config.ALGORITHMS,
                    audience=Config.AUTH0_AUDIENCE,
                    issuer=Config.AUTH0_ISSUER_BASE_URL,
                )
            except jwt.ExpiredSignatureError:
                raise AuthError(
                    {"code": "token_expired", "description": "token is expired"}, 401
                )
            except jwt.JWTClaimsError:
                raise AuthError(
                    {
                        "code": "invalid_claims",
                        "description": "incorrect claims, please check the audience and issuer",
                    },
                    401,
                )
            except Exception:
                raise AuthError(
                    {
                        "code": "invalid_header",
                        "description": "Unable to parse authentication token.",
                    },
                    401,
                )

            g.current_user = payload
            return f(*args, **kwargs)
        raise AuthError(
            {"code": "invalid_header", "description": "Unable to find appropriate key"},
            401,
        )

    return decorated
