from flask import jsonify
from db.mongodb import get_mongo_client
from analytics.analytics_repository import AnalyticsRepository
from analytics.analytics_service import AnalyticsService
from authlib.integrations.flask_oauth2 import ResourceProtector
from validator import Auth0JWTBearerTokenValidator
from os import environ as env

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    env.get("DOMAINAUTH0"),
    env.get("AUDIENCEAUTH0")
)
require_auth.register_token_validator(validator)

class AnalyticsRoutes:
    @staticmethod
    def init_app(app):
        service = AnalyticsService(AnalyticsRepository(get_mongo_client()))

        @app.route("/analytics/daily", methods=["GET"])
        @require_auth(None)  # Require authentication
        def get_daily_signalements():
            try:
                data = service.get_daily_signalements()
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route("/analytics/weekly", methods=["GET"])
        @require_auth(None)  # Require authentication
        def get_weekly_signalements():
            try:
                data = service.get_weekly_signalements()
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route("/analytics/monthly", methods=["GET"])
        @require_auth(None)  # Require authentication
        def get_monthly_signalements():
            try:
                data = service.get_monthly_signalements()
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route("/analytics/yearly", methods=["GET"])
        @require_auth(None)  # Require authentication
        def get_yearly_signalements():
            try:
                data = service.get_yearly_signalements()
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
