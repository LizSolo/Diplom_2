import allure

from api_requests import ApiRequests
from utils import generate_user_data
from data import Urls, ResponseMessages


class TestCreateOrders:
    @allure.title("Проверка создания заказа с авторизацией")
    def test_create_order_with_authorization(self):
        api_requests = ApiRequests()
        email, password, name = generate_user_data()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = api_requests.post(Urls.USER_REGISTER, json=payload)
        response_data = response.json()
        access_token = response_data['accessToken']
        headers = {
            "Authorization": access_token
        }
        ingredients_data = api_requests.get(Urls.INGREDIENTS)
        ingredient_first = ingredients_data.json()['data'][0]['_id']
        ingredient_second = ingredients_data.json()['data'][1]['_id']
        response_order = api_requests.post(Urls.ORDER, headers=headers, json={
            "ingredients": [ingredient_first, ingredient_second]
        })
        assert response_order.status_code == 200
        assert response_order.json()['success'] == True
        # удалить пользователя
        api_requests.delete(Urls.USER, headers=headers)

    @allure.title("Проверка создания заказа без авторизации")
    def test_create_order_without_authorization(self):
        api_requests = ApiRequests()
        ingredients_data = api_requests.get(Urls.INGREDIENTS)
        ingredient_first = ingredients_data.json()['data'][0]['_id']
        ingredient_second = ingredients_data.json()['data'][1]['_id']
        response_order = api_requests.post(Urls.ORDER, json={
            "ingredients": [ingredient_first, ingredient_second]
        })
        assert response_order.status_code == 200
        assert response_order.json()['success'] == True

    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_error_without_ingredients(self):
        api_requests = ApiRequests()
        response_order = api_requests.post(Urls.ORDER, json={
            "ingredients": []
        })
        assert response_order.status_code == 400
        assert response_order.json() == {'success': False, 'message': ResponseMessages.INGREDIENTS_ERROR}

    @allure.title("Проверка создания заказа с неверным хешем ингредиентов")
    def test_create_order_error_with_invalid_ingredient_id(self):
        api_requests = ApiRequests()
        response_order = api_requests.post(Urls.ORDER, json={
            "ingredients": ['ingredient_first', 'ingredient_second']
        })
        assert response_order.status_code == 500
