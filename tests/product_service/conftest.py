import random

import pytest


@pytest.fixture
def create_db_filling():
    db_dict = {}
    name = "product_name" + str(random.randint(1,10000))
    price = str(random.randint(1,10000))
    quantity = str(random.randint(1,10000))
    description = "blabla"
    db_dict["name"]=name
    db_dict["price"]=price
    db_dict["quantity"]=quantity
    db_dict["description"]=description

    return db_dict
