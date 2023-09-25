import requests


class UserService:
    url = 'http://127.0.0.1:5000'
    create_user = '/users/create'  # переменные-путь к ресурсу который будет добавлен к адресу
    get_user = 'users/'

    def __init__(self):  # метод конструктор
        pass

    def post_user(self, data):  # метод http-post на создание юзера, принимает два аргумента заголовок и данные
        r = requests.post(self.url + self.create_user,
                          json=data)  # функция внутри метода отправляет post добавляя заголовок и данные
        return r  # возвращаем результат из метода

    def get_user_id(self,data):
        r = requests.get(self.url  + '/' + self.get_user+ str(data))
        return r
