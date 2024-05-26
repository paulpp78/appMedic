from datetime import datetime, timedelta


class AnalyticsRepository:
    def __init__(self, client):
        self.db = client["signalements"]["signalements"]

    def get_daily_signalements(self):
        today = datetime.now()
        gte_today = datetime(today.year, today.month, today.day)
        lt_tomorrow = datetime(today.year, today.month, today.day + 1)
        pipeline = [
            {
                "$match": {
                    "date_created": {"$gte": gte_today, "$lt": lt_tomorrow},
                }
            },
            {"$group": {"_id": "$code_cip", "count": {"$sum": 1}}},
            {"$sort": {"_id": 1}},
        ]
        return list(self.db.aggregate(pipeline))

    def get_weekly_signalements(self):
        today = datetime.now()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=7)
        pipeline = [
            {"$match": {"date_created": {"$gte": start_of_week, "$lt": end_of_week}}},
            {
                "$group": {
                    "_id": {
                        "code_cip": "$code_cip",
                        "week": {"$week": "$date_created"},
                        "year": {"$year": "$date_created"},
                    },
                    "count": {"$sum": 1},
                }
            },
            {"$sort": {"_id": 1}},
        ]
        return list(self.db.aggregate(pipeline))

    def get_monthly_signalements(self):
        today = datetime.now()
        start_of_month = datetime(today.year, today.month, 1)
        next_month = start_of_month + timedelta(days=31)
        end_of_month = datetime(next_month.year, next_month.month, 1)
        pipeline = [
            {"$match": {"date_created": {"$gte": start_of_month, "$lt": end_of_month}}},
            {
                "$group": {
                    "_id": {
                        "code_cip": "$code_cip",
                        "month": {"$month": "$date_created"},
                        "year": {"$year": "$date_created"},
                    },
                    "count": {"$sum": 1},
                }
            },
            {"$sort": {"_id": 1}},
        ]
        return list(self.db.aggregate(pipeline))

    def get_yearly_signalements(self):
        today = datetime.now()
        start_of_year = datetime(today.year, 1, 1)
        end_of_year = datetime(today.year + 1, 1, 1)
        pipeline = [
            {"$match": {"date_created": {"$gte": start_of_year, "$lt": end_of_year}}},
            {
                "$group": {
                    "_id": {
                        "code_cip": "$code_cip",
                        "year": {"$year": "$date_created"},
                    },
                    "count": {"$sum": 1},
                }
            },
            {"$sort": {"_id": 1}},
        ]
        return list(self.db.aggregate(pipeline))
