import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    APP_PORT = int(os.getenv("APP_PORT", 3000))
    CORS_ORIGIN = os.getenv("CORS_ORIGIN")
    CORS_ORIGIN_PROD = os.getenv("CORS_ORIGIN_PROD")
    CORS_ORIGIN_FRONT = os.getenv("CORS_ORIGIN_FRONT")
    HOST = os.getenv("HOST", "0.0.0.0")
    AUTH0_AUDIENCE = os.getenv("AUTH0_AUDIENCE")
    AUTH0_ISSUER_BASE_URL = os.getenv("AUTH0_ISSUER_BASE_URL")
    ALGORITHMS = ["RS256"]
    AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
    API_IDENTIFIER = os.getenv("API_IDENTIFIER")
    CORS = os.getenv("CORS")
