import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    APP_PORT = int(os.getenv("APP_PORT", 3000))
