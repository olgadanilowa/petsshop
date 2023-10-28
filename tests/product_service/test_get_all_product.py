from tests.product_service.config import UserProduct

def test_get_all_products_success():
    params = {"limit":"10"}
    r = UserProduct().get_all_products(params=params)

    assert r.status_code == 200
    assert len(r.json()["result"])<=int(params["limit"])


