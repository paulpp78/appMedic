from auth.validator import Auth0JWTBearerTokenValidator
from authlib.integrations.flask_oauth2 import ResourceProtector

from config import Config

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(Config.AUTH0_DOMAIN, Config.API_IDENTIFIER)
require_auth.register_token_validator(validator)
