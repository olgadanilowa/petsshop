
from tests.order_service.config import UserOrders



def test_get_all_orders_success():
    r = UserOrders().get_all_orders(data=json)

    assert r.status_code == 200

    print(r.json)

