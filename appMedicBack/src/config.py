import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    APP_PORT = int(os.getenv("APP_PORT", 3000))
    CORS_ORIGIN = os.getenv("CORS_ORIGIN")
    CORS_ORIGIN_FRONT = os.getenv("CORS_ORIGIN_FRONT")
    CORS_ORIGIN_PROD = os.getenv("CORS_ORIGIN_PROD")
