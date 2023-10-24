import requests


class UserProduct:
    url = 'http://127.0.0.1:5000'
    create_product_endpoint = '/goods/create'
    get_all_product_endpoint = 'goods/all'
    get_product_endpoint = 'goods/'
    update_product_endpoint = 'update/'
    delete_product_endpoint = 'delete/'


    def __init__(self):
        pass

    def get_all_products(self, headers):
        r = requests.get(self.url + '/' + self.get_all_product_endpoint, headers=headers)
        return r

    def create_product(self, data):
        r = requests.post(self.url + self.create_product_endpoint,
                          json=data)
        return r

    def get_product_id(self, product_id):
        r = requests.get(self.url + '/' + self.get_product_endpoint + str(product_id))
        return r

    def update_product(self, data, product_id):
        r = requests.put(self.url + '/' + self.get_product_endpoint + self.update_product_endpoint + str(product_id), json=data)
        return r

    def delete_product(self, product_id):
        r = requests.delete(self.url + '/' + self.get_product_endpoint + self.delete_product_endpoint + str(product_id))
        return r
