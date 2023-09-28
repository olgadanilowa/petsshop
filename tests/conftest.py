import random

import pytest

@pytest.fixture
def genereate_email():
    email="test_user" + str(random.randint(1, 10000) + 1) + '@' + random.choice(
        ['mail.ru', 'gmail.com', 'yandex.ru'])
    return email

@pytest.fixture
def generate_name():
    name="test_user" + str(random.randint(1, 10000) + 1)
    return name

@pytest.fixture
def create_test_users_body(genereate_email,generate_name):
    users = {}
    users["name"] = generate_name
    users["email"] = genereate_email
    users["date_birth"] = str(random.randint(1923, 2023)) + "." + str(random.randint(1, 12)) + "." + str(
        random.randint(1, 31))
    users['customer_type'] = random.choice(['private','company'])
    return users


