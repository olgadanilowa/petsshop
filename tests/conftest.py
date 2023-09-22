import random

import pytest


@pytest.fixture
def create_test_users_body():
    users = {}
    users["name"] = "test_user" + str(random.randint(1, 10000) + 1)
    users["email"] = "test_user" + str(random.randint(1, 10000) + 1) + '@' + random.choice(
        ['mail.ru', 'gmail.com', 'yandex.ru'])
    users["date_birth"] = str(random.randint(1923, 2023)) + "." + str(random.randint(1, 12)) + "." + str(
        random.randint(1, 31))
    return users
