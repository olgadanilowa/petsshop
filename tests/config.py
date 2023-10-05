import requests


class UserService:
    url = 'http://127.0.0.1:5000'
    create_user_endpoint = '/users/create'  # переменные-путь к ресурсу который будет добавлен к адресу
    get_user_endpoint = 'users/'
    update_user_endpoint = 'update/'

    def __init__(self):  # метод конструктор
        pass

    def post_user(self, data):  # метод http-post на создание юзера, принимает два аргумента заголовок и данные
        r = requests.post(self.url + self.create_user_endpoint,
                          json=data)  # функция внутри метода отправляет post добавляя заголовок и данные
        return r  # возвращаем результат из метода

    def get_user_id(self, user_id):
        r = requests.get(self.url + '/' + self.get_user_endpoint + str(user_id))
        return r

    def update_user(self, data, user_id):
        r = requests.put(self.url + '/' + self.get_user_endpoint + self.update_user_endpoint + str(user_id), json=data)
        return r
