from flask import Flask, jsonify
from models import init_app, db, User
from flask_migrate import Migrate
import requests, random

app = Flask(__name__)
app.config['SECRET_KEY'] = "opop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'
init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index_page():
    return "hophop"


@app.route("/all", methods=['GET'])
def get_all_users():
    all_users = User.query.all()
    result = [user.serialize() for user in all_users]
    response = {"message": "users", "result": result}

    return jsonify(response)


def create_test_users():
    users = {}
    for i in range(5):
        name = "test_user" + str(i + 1)
        email = "test_user" + str(i + 1) + '@' + random.choice(['mail.ru', 'gmail.com', 'yandex.ru'])
        date_birth = str(random.randint(1923, 2023)) + "." + str(random.randint(1, 12)) + "." + str(random.randint(1, 31))
        data = {'name': name, 'email': email, 'date_birth': date_birth}
        response = requests.post('http://127.0.0.1:5000/all', data=data)
        response_json = response.json()
        users[i + 1] = {'id': response_json['id'], 'name': name, 'email': email, 'date_birth': date_birth}
    return users
