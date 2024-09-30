import allure
from api_requests import ApiRequests
from conftest import user_data
from data import Urls, ResponseMessages


class TestUserUpdate:
    @allure.title("Проверка изменения имени пользователя")
    def test_user_update_name(self, user_data):
        api_requests = ApiRequests()
        email, password, name, headers = user_data

        response_update = api_requests.patch(Urls.USER, headers=headers, json={
            "name": 'new_name'
        })
        assert response_update.status_code == 200
        assert response_update.json()['user']['name'] == 'new_name'

    @allure.title("Проверка изменения email пользователя")
    def test_user_update_email(self, user_data):
        api_requests = ApiRequests()
        email, password, name, headers = user_data

        response_update = api_requests.patch(Urls.USER, headers=headers, json={
            "email": f'{email}1'
        })
        assert response_update.status_code == 200
        assert response_update.json()['user']['email'] == f'{email}1'

    @allure.title("Проверка изменения пароля пользователя")
    def test_user_update_password(self, user_data):
        api_requests = ApiRequests()
        email, password, name, headers = user_data

        response_update = api_requests.patch(Urls.USER, headers=headers, json={
            "password": 'new_password'
        })
        assert response_update.status_code == 200
        assert response_update.json()['success'] == True

    @allure.title("Проверка изменения имени пользователя без авторизации")
    def test_user_error_update_name(self):
        api_requests = ApiRequests()
        response_update = api_requests.patch(Urls.USER, json={
            "name": 'new_name'
        })
        assert response_update.status_code == 401
        assert response_update.json() == {'success': False, 'message': ResponseMessages.AUTHORISED_ERROR}