class SignalementRepository:
    def __init__(self, db):
        self.db = db

    def update(self, signalement_id, update_data):
        result = self.db.signalements.update_one(
            {"_id": signalement_id}, {"$set": update_data}
        )
        return result.modified_count
    
    def insert(self, signalement_id, created_data):
        result = self.db.signalements.update_one(
            {"_id": signalement_id}, {"$insert": created_data}
        )
        return result.created_count