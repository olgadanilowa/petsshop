from tests.user_service.config import UserService
from tests.user_service.db_config import DbConnect


def test_get_all_users():
    headers={'X-Api-Key':'hophop'}

    r = UserService().get_all_users(headers=headers)

    assert r.status_code==200
    assert len(r.json()['result'])==DbConnect().count_users_db()


def test_headers_wrong():
    headers={'X-Api-Key':'opop'}

    r = UserService().get_all_users(headers=headers)

    assert r.status_code==401


def test_no_header():
    headers={'opop':'opop'}

    r = UserService().get_all_users(headers=headers)

    assert r.status_code==401

