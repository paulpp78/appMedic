Write-Host "Installation des dépendances du backend..."
cd appMedicBack
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

Write-Host "Installation des dépendances du frontend..."
cd ..\appMedicFront
npm install

Write-Host "L'installation est terminée."
