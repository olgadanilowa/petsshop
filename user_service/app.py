import json

from flask import Flask, jsonify, request
from models import init_app, db, User
from flask_migrate import Migrate
import sqlalchemy


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


@app.route("/users/create", methods=['POST'])
def create_user_db():
    try:
        user=User()
        user.name=json.loads(request.data)["name"]
        user.email=json.loads(request.data)["email"]
        user.date_birth=json.loads(request.data)["date_birth"]
        db.session.add(user)
        db.session.commit()
        response = {"message":"User added"}
        return jsonify(response),201
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        response = {"message":"User already exists"}
        return  jsonify(response), 400

