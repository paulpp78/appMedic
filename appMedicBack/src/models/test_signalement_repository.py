import pytest
from faker import Faker
from signalement import Signalement

fake = Faker()

@pytest.fixture
def signalement_ids():
    return [fake.uuid4() for _ in range(10)]

def test_delete_signalement(signalement_ids, repository):
    # Créer les signalements avec les IDs générés
    for signalement_id in signalement_ids:
        # Ajouter le signalement à la base de données
        # Ceci est une simulation, vous devrez remplacer cette logique par votre propre logique pour ajouter le signalement à la base de données
        pass

    # Supprimer un signalement
    deleted_signalement_id = signalement_ids[0]
    repository.delete(deleted_signalement_id)
    print(f"Signalement with ID {deleted_signalement_id} deleted.")

    # Récupérer tous les signalements restants
    remaining_signalements = []
    for signalement_id in signalement_ids:
        # Récupérer le signalement de la base de données
        # Ceci est une simulation, vous devrez remplacer cette logique par votre propre logique pour récupérer le signalement de la base de données
        signalement = repository.get(signalement_id)
        if signalement is not None:
            remaining_signalements.append(signalement)

    # Vérifier qu'il reste 9 signalements
    assert len(remaining_signalements) == 9
    print("Number of remaining signalements:", len(remaining_signalements))

    # Vérifier que le signalement supprimé n'est plus dans la liste des signalements restants
    assert deleted_signalement_id not in [signalement.id for signalement in remaining_signalements]
    print(f"Signalement with ID {deleted_signalement_id} not found in remaining signalements.")
