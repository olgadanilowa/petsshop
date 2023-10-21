import json

import jsonschema
import sqlalchemy
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from sqlalchemy import select

from models import init_app, db, Goods
from schemas import GoodsSchemas

app = Flask(__name__)
app.config['SECRET_KEY'] = "opop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/goods.db'
init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index_page():
    return "hophop"


@app.route("/all", methods=['GET'])
def get_all_goods():
    all_goods = Goods.query.all()
    result = [goods.serialize() for goods in all_goods]
    response = {"message": "All goods", "result": result}

    return jsonify(response)


@app.route("/goods/create", methods=['POST'])
def create_goods_db():
    try:
        goods = Goods()
        jsonschema.validate(instance=json.loads(request.data), schema=GoodsSchemas.create_goods)
        goods.name = json.loads(request.data)["name"]
        goods.price = json.loads(request.data)["price"]
        goods.quantity = json.loads(request.data)["quantity"]
        goods.description = json.loads(request.data)["description"]
        db.session.add(goods)
        db.session.commit()
        response = {"message": "Product added", "result": goods.serialize()}
        return jsonify(response), 201
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        response = {"message": "Product already exists"}
        return jsonify(response), 400
    except KeyError:
        db.session.rollback()
        response = {"message": "Fill all fields"}
        return jsonify(response), 400
    except jsonschema.exceptions.ValidationError:
        db.session.rollback()
        response = {"message": "Check the fields"}
        return jsonify(response), 400


@app.route("/goods/<product_id>", methods=['GET'])
def get_product_id_information(product_id):
    select_product = db.session.execute(select(Goods).filter_by(id=product_id))
    goods = next(select_product)[0]
    response = {"message": "Info successfully acquired", "result": goods.serialize()}

    return jsonify(response), 200


@app.route("/goods/update/<product_id>", methods=['PUT'])
def update_goods_db(product_id):
    try:
        select_product = db.session.execute(select(Goods).filter_by(id=product_id))
        goods = next(select_product)[0]
        jsonschema.validate(instance=json.loads(request.data), schema=GoodsSchemas.create_goods)
        goods.name = json.loads(request.data)["name"]
        goods.price = json.loads(request.data)["price"]
        goods.quantity = json.loads(request.data)["quantity"]
        goods.description = json.loads(request.data)["description"]
        db.session.add(goods)
        db.session.commit()
        response = {"message": "Goods updated", "result": goods.serialize()}
        return jsonify(response), 200
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        response = {"message": "Product with such data already exists"}
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
        response = {"message": "Product not found"}
        return jsonify(response), 400


@app.route("/goods/delete/<product_id>", methods=['DELETE'])
def delete_product(product_id):
    try:
        select_product = db.session.execute(select(Goods).filter_by(id=product_id))
        goods = next(select_product)[0]
        db.session.delete(goods)
        db.session.commit()
        response = {"message":"Product deleted"}
        return jsonify(response), 200
    except StopIteration:
        db.session.rollback()
        response = {"message": "Product not found"}
        return jsonify(response), 404

