# auth.py
from functools import wraps
from flask import request, jsonify
from authlib.integrations.flask_oauth2 import ResourceProtector
from validator import Auth0JWTBearerTokenValidator
from os import environ as env

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    env.get("DOMAINAUTH0"),
    env.get("AUDIENCEAUTH0")
)
require_auth.register_token_validator(validator)

def requires_role(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization', None).split()[1]
            claims = validator.decode_token(token)
            if role not in claims.get('permissions', []):
                return jsonify({"error": "Unauthorized"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator
