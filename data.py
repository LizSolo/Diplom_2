class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    USER_REGISTER = 'auth/register'
    USER_LOGIN = 'auth/login'
    USER = 'auth/user'
    ORDER = 'orders'
    INGREDIENTS = 'ingredients'

class ResponseMessages:
    AUTH_ERROR_REGISTER ='User already exists'
    AUTH_ERROR_MISS_FIELDS = 'Email, password and name are required fields'
    LOGIN_ERROR ='email or password are incorrect'
    AUTHORISED_ERROR = 'You should be authorised'
    INGREDIENTS_ERROR = 'Ingredient ids must be provided'
