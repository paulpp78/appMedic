from flask import Flask, jsonify, Response
from flask_cors import CORS

from analytics.analytics_routes import AnalyticsRoutes
from config import Config
from db.mongodb import get_mongo_client
from route.SignalementRoutes import SignalementRoutes
from utils import AuthError

app = Flask(__name__)

initialized = False

CORS(app, origins=[Config.CORS_ORIGIN, Config.CORS_ORIGIN_FRONT, Config.CORS_ORIGIN_PROD, Config.CORS, ],
    allow_headers=["Content-Type", "Authorization"], )


@app.errorhandler(AuthError)
def handle_auth_error(ex: AuthError) -> Response:
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


# @app.before_request
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


@app.errorhandler(401)
def custom_401(error):
    return jsonify({"message": "Authentication is required"}), 401


AnalyticsRoutes.init_app(app)
SignalementRoutes.init_app(app)
if __name__ == "__main__":
    initialize_database()
    app.run(host=Config.HOST, debug=True, port=Config.APP_PORT)
