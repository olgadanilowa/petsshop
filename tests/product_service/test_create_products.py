from tests.product_service.config import UserProduct
from tests.product_service.static import Errors, SuccessResponseProducts
import pytest

def _succesful_check_create_products(r, create_db_filling):
    assert r.status_code == 201
    assert r.json()['message'] == SuccessResponseProducts.created['message']
    assert r.json()['result']['name'] == create_db_filling['name']
    assert r.json()['result']['price'] == create_db_filling['price']
    assert r.json()['result']['quantity'] == create_db_filling['quantity']
    assert r.json()['result']['description'] == create_db_filling['description']


def test_create_product(create_db_filling):
    r = UserProduct().create_product(data=create_db_filling)

    _succesful_check_create_products(r, create_db_filling)

def test_create_product_without_name(create_db_filling):
    data = create_db_filling
    data.pop("name")

    r = UserProduct().create_product(data=data)

    assert r.status_code == 400
    assert r.json() == Errors.incorrect_fields

@pytest.mark.parametrize("invalid_price",["", "1a", "!@#", "-1", "None", "3.14159"])
def test_create_product_with_invalid_price(create_db_filling, invalid_price):

    data = create_db_filling
    data["price"] = invalid_price

    r = UserProduct().create_product(data=data)

    assert r.status_code == 400
    assert r.json() == Errors.incorrect_fields


def test_create_product_with_large_description(create_db_filling):
    data = create_db_filling
    data["description"] = 'a' * 201

    r = UserProduct().create_product(data=data)

    assert r.status_code == 400
    assert r.json() == Errors.incorrect_fields

def test_create_product_invalid_quantity(create_db_filling):
    data = create_db_filling
    data["quantity"] = 'пять'

    r = UserProduct().create_product(data=data)

    assert r.status_code == 400
    assert r.json() == Errors.incorrect_fields
