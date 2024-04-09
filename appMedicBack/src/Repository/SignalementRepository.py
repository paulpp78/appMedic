class SignalementRepository:
    def __init__(self, db):
        self.db = db

    def update(self, signalement_id, update_data):
        result = self.db.signalements.signalements.update_one(
            {"_id": signalement_id}, {"$set": update_data}
        )
        return result.modified_count

    def create(self, created_data):
        result = self.db.signalements.signalements.insert_one(created_data)
        return result.acknowledged

    def delete(self, signalement_id):
        query = {"_id": signalement_id}
        result = self.db.signalements.delete_one(query)
        return result.deleted_count

    def read(self, signalement_id):
        query = {"_id": signalement_id}
        result = self.db.signalements.find_one(query)
        return result

    def read_all(self):
        result = self.db.signalements.signalements.find()
        return result
