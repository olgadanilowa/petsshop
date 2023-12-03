from tests.product_service.config import UserProduct
import  pytest

def test_create_basket():

    data = {"user_id":"1", "product_id":"1", "quantity":"5"}
    r = UserProduct().create_basket(data = data)
    print(r.json())
