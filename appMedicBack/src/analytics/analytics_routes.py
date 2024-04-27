from flask import jsonify
from db.mongodb import get_mongo_client
from analytics.analytics_repository import AnalyticsRepository
from analytics.analytics_service import AnalyticsService


class AnalyticsRoutes:
    @staticmethod
    def init_app(app):
        service = AnalyticsService(AnalyticsRepository(get_mongo_client()))

        @app.route("/analytics/daily", methods=["GET"])
        def get_daily_signalements():
            try:
                data = service.get_daily_signalements()
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route("/analytics/weekly", methods=["GET"])
        def get_weekly_signalements():
            try:
                data = service.get_weekly_signalements()
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route("/analytics/monthly", methods=["GET"])
        def get_monthly_signalements():
            try:
                data = service.get_monthly_signalements()
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route("/analytics/yearly", methods=["GET"])
        def get_yearly_signalements():
            try:
                data = service.get_yearly_signalements()
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
