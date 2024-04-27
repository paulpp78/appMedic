class AnalyticsService:
    def __init__(self, repository):
        self.repository = repository

    def get_daily_signalements(self):
        return self.repository.get_daily_signalements()

    def get_weekly_signalements(self):
        return self.repository.get_weekly_signalements()

    def get_monthly_signalements(self):
        return self.repository.get_monthly_signalements()

    def get_yearly_signalements(self):
        return self.repository.get_yearly_signalements()
