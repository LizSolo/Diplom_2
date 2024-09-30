import requests
import allure
from data import Urls

class ApiRequests:
    def __init__(self):
        self.base_url = Urls.BASE_URL

    @allure.step("Отправка POST-запроса на эндпоинт: {endpoint}")
    def post(self, endpoint, headers=None, json=None):
        url = f'{self.base_url}{endpoint}'
        return requests.post(url, headers=headers, json=json)

    @allure.step("Отправка GET-запроса на эндпоинт: {endpoint}")
    def get(self, endpoint, headers=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url,  headers=headers,json=json)

    @allure.step("Отправка DELETE-запроса на эндпоинт: {endpoint}")
    def delete(self, endpoint, headers=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url, headers=headers, json=json)

    @allure.step("Отправка PATCH-запроса на эндпоинт: {endpoint}")
    def patch(self, endpoint, headers=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.patch(url, headers=headers, json=json)