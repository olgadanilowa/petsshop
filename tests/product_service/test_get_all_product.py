from tests.product_service.config import UserProduct

def test_get_all_products_success():
    headers = {"limit":"10"}
    r = UserProduct().get_all_products(headers=headers)

    assert r.status_code == 200
    print(r.json())

