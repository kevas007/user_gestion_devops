import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS

# Chargement des variables d'environnement
load_dotenv()

# Initialisation de l'application
app = Flask(__name__)

# Configuration CORS plus permissive
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}}, allow_headers="*")

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
    f"@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle d'exemple
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Fonction pour alimenter la base de données avec des données initiales
def seed_database():
    # Liste des usernames à garantir
    usernames = ["admin", "user1", "user2", "test_user", "demo_account"]
    added = []

    for username in usernames:
        if not User.query.filter_by(username=username).first():
            db.session.add(User(username=username))
            added.append(username)

    if added:
        db.session.commit()
        print(f"{len(added)} utilisateurs ajoutés : {added}")
    else:
        print("Aucun utilisateur manquant, seed skipped.")

    return added

# Création des tables immédiatement à l'import
with app.app_context():
    db.create_all()

# Routes CRUD basiques
@app.route('/api/users', methods=['GET'])
def list_users():
    return jsonify([{'id': u.id, 'username': u.username} for u in User.query.all()])

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(username=data['username'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username}), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)
    user.username = data['username']
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username})

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

# OPTIONS route pour CORS preflight
@app.route('/api/seed', methods=['OPTIONS'])
def seed_options():
    return '', 200

# Route de seeding principale
@app.route('/api/seed', methods=['POST'])
def seed_route():
    print("Route /api/seed appelée")
    try:
        added = seed_database()
        return jsonify({
            'message': 'Database seeded successfully',
            'new_users_added': len(added),
            'added_usernames': added
        }), 200
    except Exception as e:
        print(f"Erreur pendant le seeding: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Routes alternatives de seeding
@app.route('/seed', methods=['GET', 'POST'])
def seed_direct():
    print("Route directe /seed appelée")
    try:
        added = seed_database()
        return jsonify({
            'message': 'Database seeded successfully',
            'new_users_added': len(added),
            'added_usernames': added
        }), 200
    except Exception as e:
        print(f"Erreur pendant le seeding: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/seed', methods=['GET', 'POST'])
def seed_users_route():
    print("Route alternative /api/users/seed appelée")
    try:
        added = seed_database()
        return jsonify({
            'message': 'Database seeded successfully',
            'new_users_added': len(added),
            'added_usernames': added
        }), 200
    except Exception as e:
        print(f"Erreur pendant le seeding: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Route de test simple
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200

# Afficher toutes les routes au démarrage pour vérification
print("Routes enregistrées:")
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint}: {rule.methods} - {rule}")

if __name__ == '__main__':
    print(f"Serveur démarré sur http://0.0.0.0:3000")
    app.run(host='0.0.0.0', port=3000, debug=True)  # Debug mode activé