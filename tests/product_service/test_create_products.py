from tests.product_service.config import UserProduct

def test_create_product(create_db_filling):
    r = UserProduct().create_product(data=create_db_filling)
    print(r.json())
