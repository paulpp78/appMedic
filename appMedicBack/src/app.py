from flask import Flask, jsonify
from flask_cors import CORS
from db.mongodb import get_mongo_client
from route.SignalementRoutes import SignalementRoutes
from analytics.analytics_routes import AnalyticsRoutes
from config import Config  # Assurez-vous que cette ligne est présente
from validator import Auth0JWTBearerTokenValidator
from authlib.integrations.flask_oauth2 import ResourceProtector

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    "appmedic-for-you.eu.auth0.com",
    "https://appMedic-api.fr"
)
require_auth.register_token_validator(validator)

app = Flask(__name__)
initialized = False

CORS(
    app,
    origins=[
        Config.CORS_ORIGIN,
        Config.CORS_ORIGIN_FRONT,
        Config.CORS_ORIGIN_PROD,
    ],
)
