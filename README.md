Примеры запросов for Users:

# Регистрация пользователя и получение confirmation_code
###
POST http://127.0.0.1:8000/api/v1/auth/signup/
Content-Type: application/json

{
    "email": "user@mail.ru",
    "username": "user"
}


# Получение токена пользователя
###
POST http://127.0.0.1:8000/api/v1/auth/token/
Content-Type: application/json

{
    "username": "user2",
    "confirmation_code": "65y-64a6e988500b2eeac0b"
}

# Получить данные своей учетной записи
###
GET  http://127.0.0.1:8000/api/v1/users/me/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4OTQ4Njc1LCJqdGkiOiJjYmE4NGMzZGUzYjI0ODA5OTY3ZjJiODZiOTM2YjQzYiIsInVzZXJfaWQiOjV9.guSbTtW-YBKsmOYzwzE7xu0tPXQ7dMoI2YzbAi4ZSw8


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


# Получение списка всех пользователей с токеном Админа
###
GET   http://127.0.0.1:8000/api/v1/users/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4ODc3NTUzLCJqdGkiOiJmOGI5NDNhMjY5Mjk0MWNkOGQzZmQyYzk4N2JlODljOSIsInVzZXJfaWQiOjJ9.rw69vzp1RU80K-2PHiGPjRVm3umj0cKCaAy5ulZ7xJc
Content-Type: application/json


# Получаем token admin
###
POST http://127.0.0.1:8000/api/v1/auth/token/
Content-Type: application/json

{
    "username": "admin"
}