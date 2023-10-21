import json

import jsonschema
import sqlalchemy
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from sqlalchemy import select

from models import init_app, db, Order


app = Flask(__name__)
app.config['SECRET_KEY'] = "opop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/orders.db'
init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index_page():
    return "hophop"


@app.route('/all', methods=['GET'])
def get_all_orders():
    orders=Order.query.all()
    result=[order.serialize() for order in orders]
    response = {'message':'All orders found', 'result':result}
    return jsonify(response), 200
