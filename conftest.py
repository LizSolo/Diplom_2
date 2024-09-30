# conftest.py
import pytest
from api_requests import ApiRequests
from data import Urls
from utils import generate_user_data


@pytest.fixture
def user_data():
    api_requests = ApiRequests()

    # Генерация данных пользователя
    email, password, name = generate_user_data()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # Регистрация пользователя
    response = api_requests.post(Urls.USER_REGISTER, json=payload)
    response_data = response.json()
    access_token = response_data['accessToken']
    headers = {
        "Authorization": access_token
    }

    # Возвращаем данные пользователя и заголовок авторизации
    yield email, password, name, headers

    # Удаление пользователя после завершения теста
    api_requests.delete(Urls.USER, headers=headers)
