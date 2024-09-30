import allure
from api_requests import ApiRequests
from conftest import user_data
from data import Urls, ResponseMessages


class TestLogin:
    @allure.title("Проверка, что пользователь может авторизоваться")
    def test_login_user(self, user_data):
        api_requests = ApiRequests()
        email, password, name, headers = user_data

        # Пытаемся авторизоваться
        payload_login = {
            "email": email,
            "password": password
        }
        response = api_requests.post(Urls.USER_LOGIN, json=payload_login)
        response_data = response.json()

        assert response.status_code == 200
        assert response_data['user']['email'] == email
        assert response_data['user']['name'] == name

    @allure.title("Проверка, что пользователь не может авторизоваться с неверным логином")
    def test_login_user_error_nonexistent_email(self, user_data):
        api_requests = ApiRequests()
        email, password, name, headers = user_data

        # Пытаемся авторизоваться с неверным email
        payload_login = {
            "email": f'{email}g',  # Добавляем 'g' к email
            "password": password
        }
        response = api_requests.post(Urls.USER_LOGIN, json=payload_login)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': ResponseMessages.LOGIN_ERROR}

    @allure.title("Проверка, что пользователь не может авторизоваться с неверным паролем")
    def test_login_user_error_nonexistent_password(self, user_data):
        api_requests = ApiRequests()
        email, password, name, headers = user_data

        # Пытаемся авторизоваться с неверным паролем
        payload_login = {
            "email": email,
            "password": f'{password}2'  # Добавляем '2' к паролю
        }
        response = api_requests.post(Urls.USER_LOGIN, json=payload_login)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': ResponseMessages.LOGIN_ERROR}
