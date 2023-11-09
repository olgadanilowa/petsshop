import requests


class UserService:
    url = 'http://127.0.0.1:5000'
    create_user_endpoint = '/users/create'
    all_users_endpoint = '/all'
    get_user_endpoint = 'users/'
    update_user_endpoint = 'update/'
    delete_user_endpoint = 'delete/'
    user_login_endpoint = '/login'

    def __init__(self):
        pass

    def get_all_users(self, headers):
        r = requests.get(self.url + self.all_users_endpoint, headers=headers)
        return r

    def user_login(self, data):
        r = requests.post(self.url + self.user_login_endpoint, json=data)
        return r

    def post_user(self, data):
        r = requests.post(self.url + self.create_user_endpoint, json=data)
        return r

    def get_user_id(self, user_id, headers):
        r = requests.get(self.url + '/' + self.get_user_endpoint + str(user_id), headers=headers)
        return r

    def update_user(self, data, user_id, headers):
        r = requests.put(self.url + '/' + self.get_user_endpoint + self.update_user_endpoint + str(user_id), json=data,
                         headers=headers)
        return r

    def delete_user(self, user_id, headers):
        r = requests.delete(self.url + '/' + self.get_user_endpoint + self.delete_user_endpoint + str(user_id),
                            headers=headers)
        return r
