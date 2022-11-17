Примеры запросов for Users:

# Регистрация пользователя
###
POST http://127.0.0.1:8000/api/v1/auth/signup/
Content-Type: application/json

{
    "email": "user2@mail.ru",
    "username": "user2"
}


# Получение токена пользователя
###
POST http://127.0.0.1:8000/api/v1/auth/token/
Content-Type: application/json

{
    "username": "user2",
    "confirmation_code": "65y-64a6e988500b2eeac0bb"
}

# Получить данные своей учетной записи
###
GET  http://127.0.0.1:8000/api/v1/users/me/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4ODA0ODU3LCJqdGkiOiIyZjEzZWMzZWM1MDU0ODI0OTU1ZmUwM2Y4MmE2NDU2NSIsInVzZXJfaWQiOjV9.bzQTBMpOjztnhLwo-rXGQXY7eqwzyX23XtqkMq0f22U


# Изменить данные своей учетной записи
###
PATCH http://127.0.0.1:8000/api/v1/users/me/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4ODA0ODU3LCJqdGkiOiIyZjEzZWMzZWM1MDU0ODI0OTU1ZmUwM2Y4MmE2NDU2NSIsInVzZXJfaWQiOjV9.bzQTBMpOjztnhLwo-rXGQXY7eqwzyX23XtqkMq0f22U
Content-Type: application/json

{
    "username": "user2",
    "email": "user2@mail.ru",
    "first_name": "User",
    "last_name": "user",
    "bio": "",
    "role": "user"
}
