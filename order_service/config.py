import requests


class UserOrders:
    url = 'http://127.0.0.1:5000'
    all_orders = 'orders/'


    def __init__(self):
        pass


    def get_all_orders():
        r = requests.get(self.url + '/' + self.all_orders)
        return r
