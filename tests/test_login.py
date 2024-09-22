import allure
from api_requests import ApiRequests
from utils import generate_user_data
from data import Urls, ResponseMessages

class TestLogin:
    @allure.title("Проверка, что пользователь может авторизоваться")
    def test_login_user(self):
        api_requests = ApiRequests()
        email, password, name = generate_user_data()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        api_requests.post(Urls.USER_REGISTER, json=payload)
        response = api_requests.post(Urls.USER_LOGIN, json=payload)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['user']['email'] == email
        assert response_data['user']['name'] == name
        # удалить пользователя
        access_token = response_data['accessToken']
        headers = {
            "Authorization": access_token
        }
        api_requests.delete(Urls.USER, headers=headers)

    @allure.title("Проверка, что пользователь не может авторизоваться с неверным логином")
    def test_login_user_error_nonexistent_email(self):
        api_requests = ApiRequests()
        email, password, name = generate_user_data()
        payload_auth = {
            "email": email,
            "password": password,
            "name": name
        }
        response_data = api_requests.post(Urls.USER_REGISTER, json=payload_auth).json()
        payload_login = {
            "email": f'{email}g',
            "password": password
        }
        response = api_requests.post(Urls.USER_LOGIN, json=payload_login)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': ResponseMessages.LOGIN_ERROR}
        # удалить пользователя
        access_token = response_data['accessToken']
        headers = {
            "Authorization": access_token
        }
        api_requests.delete(Urls.USER, headers=headers)

    @allure.title("Проверка, что пользователь не может авторизоваться с неверным паролем")
    def test_login_user_error_nonexistent_password(self):
        api_requests = ApiRequests()
        email, password, name = generate_user_data()
        payload_auth = {
            "email": email,
            "password": password,
            "name": name
        }
        response_data =api_requests.post(Urls.USER_REGISTER, json=payload_auth).json()
        payload_login = {
            "email": email,
            "password": f'{password}2'
        }
        response = api_requests.post(Urls.USER_LOGIN, json=payload_login)
        assert response.status_code == 401
        assert  response.json() == {'success': False, 'message': ResponseMessages.LOGIN_ERROR}
        # удалить пользователя
        access_token = response_data['accessToken']
        headers = {
            "Authorization": access_token
        }
        api_requests.delete(Urls.USER, headers=headers)