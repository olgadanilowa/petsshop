import json
import jsonschema
import random
import sqlalchemy
import string
from datetime import datetime
from flask import Flask, jsonify, request
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
    return "hophop"


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
                message = {"message": "Successful authentication"}
                status_code = 200
                user.token = ''.join(random.choice(string.ascii_letters) for i in range(15))
                user.token_issue_time = datetime.now().time()
                db.session.commit()
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
    def decorator(*args, **kwargs):
        if 'x-auth-token' in request.headers or 'email' in request.headers:
            token = request.headers['x-auth-token']
            email = request.headers['email']
            try:
                user_select = db.session.execute(select(User).filter_by(email=email))
                user = next(user_select)[0]
                if 'token' in user.serialize().keys():
                    if user.serialize()['token'] == token:
                        message = {"message": "Successful authentication"}
                        return f(jsonify(message), *args, **kwargs)
                    else:
                        message = {"message": "A valid token is missing!"}
                        return f(jsonify(message), *args, **kwargs)
                else:
                    message = {"message": "A valid token is missing!"}
                    return f(jsonify(message), *args, **kwargs)
        else:
            message = {"message": "A valid token is missing!"}
            return f(jsonify(message), *args, **kwargs)
        return decorator


@app.route("/users/<user_id>", methods=['GET'])
def get_information_id(user_id):
    user_select = db.session.execute(select(User).filter_by(id=user_id))
    user = next(user_select)[0]
    response = {"message": "Info successfully acquired", "result": user.serialize()}

    return jsonify(response), 200


@app.route("/users/update/<user_id>", methods=['PUT'])
def update_user_db(user_id):
    try:
        user_select = db.session.execute(select(User).filter_by(id=user_id))
        user = next(user_select)[0]
        jsonschema.validate(instance=json.loads(request.data), schema=UserSchemas.create_user)
        user.name = json.loads(request.data)["name"]
        user.email = json.loads(request.data)["email"]
        user.customer_type = json.loads(request.data)["customer_type"]
        if "date_birth" not in json.loads(request.data).keys():
            user.date_birth = ""
        else:
            user.date_birth = json.loads(request.data)["date_birth"]
        db.session.add(user)
        db.session.commit()
        response = {"message": "User updated", "result": user.serialize()}
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

