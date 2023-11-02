import pytest

from tests.user_service.config import UserService
from tests.user_service.static import Errors


def test_user_delete_success(create_test_users_body):
    r = UserService().post_user(data=create_test_users_body)

    assert r.status_code == 201

    user_id=r.json()["result"]["id"]
    r1 = UserService().delete_user(user_id=user_id)

    assert  r1.status_code == 200
    assert r1.json() == Errors.user_deleted


def test_delete_not_exist_user(create_test_users_body):
    r = UserService().post_user(data=create_test_users_body)

    assert r.status_code == 201

    user_id = r.json()["result"]["id"]

    r1 = UserService().delete_user(user_id=user_id)

    assert r1.status_code == 200
    assert r1.json() == Errors.user_deleted

    r2 = UserService().delete_user(user_id=user_id)

    assert r2.status_code == 404
    assert r2.json() == Errors.user_not_found


@pytest.mark.parametrize("invalid_id",[1098,"pupkin","!"])
def test_user_delete_invalid_id_int(invalid_id):

    r = UserService().delete_user(user_id=invalid_id)

    assert r.status_code == 404

    assert r.json() == Errors.user_not_found

