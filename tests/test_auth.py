import allure
from api_requests import ApiRequests
from data import Urls, ResponseMessages
from utils import generate_user_data


class TestAuth:
    @allure.title("Проверка создания уникального пользователя")
    def test_auth(self):
        api_requests = ApiRequests()
        email, password, name = generate_user_data()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = api_requests.post(Urls.USER_REGISTER, json=payload)
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

    @allure.title("Проверка создания пользователя, который уже зарегистрирован")
    def test_auth_error_user_register(self):
        api_requests = ApiRequests()
        email, password, name = generate_user_data()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        api_requests.post(Urls.USER_REGISTER, json=payload)
        response = api_requests.post(Urls.USER_REGISTER, json=payload)
        assert response.status_code == 403
        assert response.json() == {'success': False, 'message': ResponseMessages.AUTH_ERROR_REGISTER}

    @allure.title("Проверка создания пользователя без имени")
    def test_auth_error_miss_field_name(self):
        api_requests = ApiRequests()
        email, password, name = generate_user_data()
        payload = {
            "email": email,
            "password": password
        }
        response = api_requests.post(Urls.USER_REGISTER, json=payload)
        assert response.status_code == 403
        assert response.json() == {'success': False, 'message': ResponseMessages.AUTH_ERROR_MISS_FIELDS}

    @allure.title("Проверка создания пользователя без email")
    def test_auth_error_miss_field_email(self):
        api_requests = ApiRequests()
        email, password, name = generate_user_data()
        payload = {
            "password": password,
            "name": name
        }
        response = api_requests.post(Urls.USER_REGISTER, json=payload)
        assert response.status_code == 403
        assert response.json() == {'success': False, 'message': ResponseMessages.AUTH_ERROR_MISS_FIELDS}

    @allure.title("Проверка создания пользователя без пароля")
    def test_auth_error_miss_field_password(self):
        api_requests = ApiRequests()
        email, password, name = generate_user_data()
        payload = {
            "email": email,
            "name": name
        }
        response = api_requests.post(Urls.USER_REGISTER, json=payload)
        assert response.status_code == 403
        assert response.json() == {'success': False, 'message': ResponseMessages.AUTH_ERROR_MISS_FIELDS}

