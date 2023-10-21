from products_service import UserProduct

def test_get_all_products_success():
    r = UserProduct().get_all_orders(json=data)

    assert r.status_code == 200
