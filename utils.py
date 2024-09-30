import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_email(length):
    domain = 'test.ru'
    random_string = generate_random_string(length)
    return f'{random_string}@{domain}'

def generate_user_data():
    email = generate_random_email(10)
    password = generate_random_string(10)
    name = generate_random_string(10)
    return email, password, name

email, password, name = generate_user_data()
print(f"Generated Email: {email}")
print(f"Generated Password: {password}")
print(f"Generated Name: {name}")


