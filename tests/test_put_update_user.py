from tests.config import UserService


def test_update_user(create_test_users_body,genereate_email,generate_name):
    r = UserService().post_user(data=create_test_users_body)
    assert r.status_code==201

    user_id = r.json()['result']['id']
    create_test_users_body["name"]=generate_name
    create_test_users_body["email"]=genereate_email
    create_test_users_body["customer_type"]="private"
    r=UserService().update_user(data=create_test_users_body,user_id=user_id)
    assert r.status_code==200
