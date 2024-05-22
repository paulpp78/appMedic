# Utiliser une image de base officielle de Python
FROM python:latest

# Installer des dépendances supplémentaires si nécessaire
RUN apt-get update && apt-get install -y build-essential

# Définir le répertoire de travail dans le conteneur
WORKDIR /appmedic-back

# Copier et installer les dépendances Python
COPY requirements.txt /appmedic-back
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . /appmedic-back

# Exposer le port utilisé par l'application
EXPOSE 3000

# Lancer l'application
CMD ["python", "src/app.py"]