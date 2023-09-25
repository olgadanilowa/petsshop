import json

import sqlalchemy
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from sqlalchemy import select

from models import init_app, db, User

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
        user = User()
        user.name = json.loads(request.data)["name"]
        user.email = json.loads(request.data)["email"]
        user.date_birth = json.loads(request.data)["date_birth"]
        db.session.add(user)
        db.session.commit()
        response = {"message": "User added"}
        return jsonify(response), 201
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        response = {"message": "User already exists"}
        return jsonify(response), 400
    except KeyError:
        db.session.rollback()
        response = {"message": "Fill all fields"}
        return jsonify(response), 400


@app.route("/users/<user_id>", methods=['GET'])
def get_information_id(user_id):
    user_select = db.session.execute(select(User).filter_by(id=user_id))
    user = next(user_select)[0]
    response = {
            "message": "Info successfully acquired",
            "result": user.serialize()
        }

    return jsonify(response), 200
