def create_test_users():
    users = {}
    for i in range(5):
        name = "test_user" + str(i + 1)
        email = "test_user" + str(i + 1) + '@' + random.choice(['mail.ru', 'gmail.com', 'yandex.ru'])
        date_birth = str(random.randint(1923, 2023)) + "." + str(random.randint(1, 12)) + "." + str(random.randint(1, 31))
        data = {'name': name, 'email': email, 'date_birth': date_birth}
        response = requests.post('http://127.0.0.1:5000/all', data=data)
        response_json = response.json()
        users[i + 1] = {'id': response_json['id'], 'name': name, 'email': email, 'date_birth': date_birth}
    return users
