import allure

from api_requests import ApiRequests
from utils import generate_user_data
from conftest import user_data
from data import Urls, ResponseMessages

class TestGetOrder:
    @allure.title("Проверка получения заказов конкретного пользователя")
    def test_get_user_orders(self, user_data):
        api_requests = ApiRequests()
        email, password, name, headers = user_data
        ingredients_data = api_requests.get(Urls.INGREDIENTS)
        ingredient_first = ingredients_data.json()['data'][0]['_id']
        ingredient_second = ingredients_data.json()['data'][1]['_id']
        api_requests.post(Urls.ORDER, headers=headers, json={
            "ingredients": [ingredient_first, ingredient_second]
        })
        response_order = api_requests.get(Urls.ORDER, headers=headers)
        assert response_order.status_code == 200
        assert response_order.json()['success'] == True
        assert len(response_order.json()['orders']) == 1

    @allure.title("Проверка получения заказов конкретного пользователя без авторизации")
    def test_get_orders_without_authorization(self):
        api_requests = ApiRequests()
        response = api_requests.get(Urls.ORDER)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': ResponseMessages.AUTHORISED_ERROR}
