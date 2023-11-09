import json
from functools import wraps

import jsonschema
import random
import sqlalchemy
import string
from datetime import datetime
from flask import Flask, jsonify, request, redirect
from flask_migrate import Migrate
from sqlalchemy import select

from models import init_app, db, User
from schemas import UserSchemas

app = Flask(__name__)
app.config['SECRET_KEY'] = "opop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'
init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index_page():
    response = {"message": "This page is empty"}
    return jsonify(response), 200


@app.route("/unlogged")
def unlogged():
    response = {"message": "You should log in before you make this request"}
    return jsonify(response), 400


@app.route("/all", methods=['GET'])
def get_all_users():
    if 'X-Api-Key' in request.headers.keys():
        if request.headers['X-Api-Key']=='hophop':
            all_users = User.query.all()
            result = [user.serialize() for user in all_users]
            response = {"message": "users", "result": result}
            return jsonify(response)
        else:
            return jsonify({"message": "ERROR: Unauthorized"}), 401
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401


@app.route("/users/create", methods=['POST'])
def create_user_db():
    try:
        user = User()
        jsonschema.validate(instance=json.loads(request.data), schema=UserSchemas.create_user)
        user.name = json.loads(request.data)["name"]
        user.email = json.loads(request.data)["email"]
        user.customer_type = json.loads(request.data)["customer_type"]
        user.password = json.loads(request.data)["password"]
        if "date_birth" not in json.loads(request.data).keys():
            user.date_birth = ""
        else:
            user.date_birth = json.loads(request.data)["date_birth"]
        db.session.add(user)
        db.session.commit()
        response = {"message": "User added", "result": user.serialize()}
        return jsonify(response), 201
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        response = {"message": "User already exists"}
        return jsonify(response), 400
    except KeyError:
        db.session.rollback()
        response = {"message": "Fill all fields"}
        return jsonify(response), 400
    except jsonschema.exceptions.ValidationError:
        db.session.rollback()
        response = {"message": "Check the fields"}
        return jsonify(response), 400


@app.route("/login", methods=['POST'])
def user_login():
    if 'password' in json.loads(request.data).keys() or 'email' in json.loads(request.data).keys():
        password = json.loads(request.data)['password']
        email = json.loads(request.data)['email']
        try:
            user_select = db.session.execute(select(User).filter_by(email=email))
            user = next(user_select)[0]
            if user.serialize()['password'] == password:
                user.token = ''.join(random.choice(string.ascii_letters) for i in range(15))
                user.token_issue_time = datetime.now().time()
                db.session.commit()
                message = {"message": "Successful authentication", "result": user.logged_in()}
                status_code = 200
            else:
                message = {"message": "A valid password or email is missing!"}
                status_code = 401
        except KeyError:
            db.session.rollback()
            response = {"message": "Make sure you are registered"}
            return jsonify(response), 400

        return jsonify(message), status_code
    else:
        return jsonify({"message": "A valid password or email is missing!"}), 401


def login_check(f):
    @wraps(f)
    def decorator(**kwargs):
        kwargs.pop('user_id')
        try:
            if request.method == "GET" and len(request.headers) > 7:
                return redirect("/unlogged")
            elif request.method == "PUT" and len(request.headers) > 9:
                return redirect("/unlogged")
            else:
                if 'x-auth-token' in request.headers and 'email' in request.headers:
                    token = request.headers['x-auth-token']
                    email = request.headers['email']
                    user_select = db.session.execute(select(User).filter_by(email=email))
                    user = next(user_select)[0]
                    if 'token' in user.logged_in().keys() and user.logged_in()['token'] == token:
                        kwargs['user_id'] = user.id
                        kwargs['result'] = user.logged_in()
                    else:
                        return redirect("/unlogged")
                else:
                    return redirect("/unlogged")
        except (KeyError, StopIteration):
            return redirect("/unlogged")
        return kwargs
    return decorator


@app.route("/users/<user_id>", methods=['GET'])
@login_check
def get_information_id(**kwargs):
    if 'user_id' in kwargs.keys():
        user_select = db.session.execute(select(User).filter_by(id=kwargs['user_id']))
        user = next(user_select)[0]
        if user.logged_in() == kwargs['result']:
            response = {"message": "Info successfully acquired", "result": kwargs['result']}
            return jsonify(response), 200
        else:
            response = {"message": "Ooops, somwthing went wrong"}
            return jsonify(response), 400
    else:
        return jsonify(kwargs), 400


@app.route("/users/update/<user_id>", methods=['PUT'])
@login_check
def update_user_db(**kwargs):
    if 'user_id' in kwargs.keys():
        try:
            user_select = db.session.execute(select(User).filter_by(id=kwargs['user_id']))
            user = next(user_select)[0]
            jsonschema.validate(instance=json.loads(request.data), schema=UserSchemas.create_user)
            if user.logged_in() == kwargs['result']:
                user.name = json.loads(request.data)["name"]
                user.email = json.loads(request.data)["email"]
                user.customer_type = json.loads(request.data)["customer_type"]
                if "date_birth" not in json.loads(request.data).keys():
                    user.date_birth = ""
                else:
                    user.date_birth = json.loads(request.data)["date_birth"]
                db.session.commit()
                response = {"message": "User updated", "result": user.logged_in()}
                return jsonify(response), 200
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            response = {"message": "User with such data already exists"}
            return jsonify(response), 400
        except KeyError:
            db.session.rollback()
            response = {"message": "Fill the fields"}
            return jsonify(response), 400
        except jsonschema.exceptions.ValidationError:
            db.session.rollback()
            response = {"message": "Check the fields"}
            return jsonify(response), 400
        except StopIteration:
            db.session.rollback()
            response = {"message": "User not found"}
            return jsonify(response), 400


@app.route("/users/delete/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    try:
        user_select = db.session.execute(select(User).filter_by(id=user_id))
        user = next(user_select)[0]
        db.session.delete(user)
        db.session.commit()
        response = {"message":"User deleted"}
        return jsonify(response), 200
    except StopIteration:
        db.session.rollback()
        response = {"message": "User not found"}
        return jsonify(response), 404

