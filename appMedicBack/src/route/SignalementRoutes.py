from flask import request, jsonify
from service.SignalementService import SignalementService
from bson import ObjectId, errors as bson_errors
from db.mongodb import get_mongo_client
from Repository.SignalementRepository import SignalementRepository

class SignalementRoutes:
    @staticmethod
    def init_app(app):
        service = SignalementService(SignalementRepository(get_mongo_client()))

        @app.route('/signalement/<signalement_id>', methods=['PUT'])
        def update_signalement(signalement_id):
            data = request.json
            pseudo, code_cip = data.get('pseudo'), data.get('code_cip')
            if not pseudo or not code_cip:
                return jsonify({"error": "Pseudo et code CIP sont requis"}), 400
            try:
                modified_count = service.update_signalement(ObjectId(signalement_id), pseudo, code_cip)
                return jsonify({"message": "Signalement mis à jour", "modified_count": modified_count}), 200
            except ValueError as ve:
                return jsonify({"error": str(ve)}), 400
            except bson_errors.InvalidId:
                return jsonify({"error": "ID de signalement invalide"}), 400
