# Backend appMedic

Bienvenue sur le backend de l'application appMedic

## Prérequis

Avant de commencer, assurez-vous que Docker est installé sur votre machine. Vous pouvez également utiliser un environnement Python local si vous préférez.

## Installation des dépendances

### Option 1 : Utilisation de Docker

1. Construisez l'image Docker :

   ```bash
   docker build -t appmedic-backend .
   ```

2. Exécutez le conteneur Docker :

   ```bash
   docker run -p 3000:3000 appmedic-backend
   ```

Votre application backend sera disponible sur `http://localhost:3000`.

### Option 2 : Environnement Python local

1. Assurez-vous que Python et pip sont installés sur votre machine.
2. Clonez le dépôt : `git clone git@github.com:paulpp78/appMedic.git`
3. Naviguez dans le dossier du backend : `cd appMedic/appMedicBack`
4. Créez et activez un environnement virtuel :

   ```bash
   python -m venv venv
   source venv/bin/activate   # Sur Windows, utilisez `venv\Scripts\activate`
   ```

5. Installez les dépendances depuis `requirements.txt` :

   ```bash
   pip install -r requirements.txt
   ```

6. Lancez l'application :

   ```bash
   flask run --host=0.0.0.0 --port=3000
   ```

Votre application backend sera disponible sur `http://localhost:3000`.

## Configuration

Assurez-vous que toutes les configurations nécessaires (comme les variables d'environnement) sont définies. Vous pouvez créer un fichier `.env` dans le répertoire racine avec les configurations nécessaires.

## Exécution des tests

Pour exécuter les tests unitaires, utilisez la commande suivante :

```bash
pytest
```

Assurez-vous que toutes les dépendances de test sont installées dans votre environnement.

## Déploiement

Pour déployer l'application, vous pouvez utiliser Docker comme décrit ci-dessus, ou configurer un serveur selon vos besoins spécifiques.

## Aide supplémentaire

Pour toute question ou problème, n'hésitez pas à consulter la documentation ou à contacter l'équipe de développement.
