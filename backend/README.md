## Backend - API Flask avec MySQL
Vue d'ensemble
Ce backend fournit une API RESTful développée avec Flask et SQLAlchemy, connectée à une base de données MySQL. L'application est conteneurisée avec Docker pour faciliter le déploiement et le développement.
Prérequis

## Docker et Docker Compose
Python 3.11 (pour le développement local)
Un environnement capable d'exécuter des conteneurs Docker

Installation et démarrage
Avec Docker (recommandé)

## Clonez le dépôt:
bashgit clone <url-du-repository>
cd <nom-du-dossier>

Lancez l'application avec Docker Compose:
bashdocker-compose up -d

L'API est accessible à l'adresse: http://localhost:3000/api/users

Développement local (sans Docker)

## Installez les dépendances:
bashcd backend
pip install -r requirements.txt

## Configurez les variables d'environnement (créez un fichier .env dans le dossier backend):
MYSQL_USER=flask_user
MYSQL_PASSWORD=flask_password
MYSQL_HOST=localhost
MYSQL_DATABASE=flask_db

Lancez l'application:
bashpython app.py


## Structure du projet
backend/
├── app.py             # Point d'entrée principal de l'application
├── Dockerfile         # Configuration Docker pour le backend
├── requirements.txt   # Dépendances Python
├── seed.py            # Script pour alimenter la base de données
└── .env               # Variables d'environnement (à créer)
## Base de données
L'application utilise MySQL comme système de gestion de base de données. Les modèles de données incluent:

User: Modèle d'exemple avec un identifiant et un nom d'utilisateur

API Endpoints
Utilisateurs

GET /api/users: Récupérer tous les utilisateurs
POST /api/users: Créer un nouvel utilisateur

Body: { "username": "example_user" }


PUT /api/users/:id: Mettre à jour un utilisateur existant

Body: { "username": "new_username" }


DELETE /api/users/:id: Supprimer un utilisateur

Seeding

POST /api/seed: Alimenter la base de données avec des données d'exemple

Header requis: X-Seed-Key: development_key



## Configuration Docker
Le backend est configuré pour s'exécuter dans un environnement Docker avec les composants suivants:

api: Le service Flask qui exécute l'application
db: Le service MySQL pour la base de données

Variables d'environnement
Les variables d'environnement suivantes peuvent être configurées:

MYSQL_USER: Nom d'utilisateur MySQL (par défaut: flask_user)
MYSQL_PASSWORD: Mot de passe MySQL (par défaut: flask_password)
MYSQL_HOST: Hôte MySQL (par défaut: db)
MYSQL_DATABASE: Nom de la base de données (par défaut: flask_db)
SEED_KEY: Clé pour l'endpoint de seeding (par défaut: development_key)

Dépannage
Problèmes courants

Erreur de connexion à la base de données:

Assurez-vous que le service MySQL est en cours d'exécution
Vérifiez les informations d'identification dans le fichier .env
Exécutez docker-compose logs db pour vérifier les journaux de MySQL


Erreur "Method Not Allowed" lors de l'accès à /api/seed:

Utilisez une requête POST au lieu de GET
Utilisez curl ou Postman avec l'en-tête X-Seed-Key approprié:
bashcurl -X POST http://localhost:3000/api/seed -H "X-Seed-Key: development_key"



Versions incompatibles des bibliothèques:

Les versions dans requirements.txt sont soigneusement sélectionnées pour garantir la compatibilité
Si vous rencontrez des erreurs, ne modifiez pas les versions sans comprendre les dépendances



Développement
Intégration de nouveaux modèles

Ajoutez votre modèle dans app.py
Mettez à jour seed.py pour inclure des données pour votre nouveau modèle
Créez les endpoints API correspondants

Exécution des tests
Pour exécuter les tests (à implémenter):
bash# À venir

Développé avec ❤️ pour le projet DevOps
