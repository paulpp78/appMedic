from flask import Flask
from config import Config
from db.mongodb import get_mongo_client
from route.SignalementRoutes import SignalementRoutes

app = Flask(__name__)

SignalementRoutes.init_app(app)

initialized = False


@app.before_request
def initialize_database():
    global initialized
    if not initialized:
        client = get_mongo_client()
        try:
            client.admin.command("ping")
            print("MongoDB connection established successfully")
            initialized = True
        except Exception as e:
            print(f"MongoDB connection failed: {e}")


if __name__ == "__main__":
    app.run(debug=True, port=Config.APP_PORT)
