# Проект YaMDb
### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

### Технологии
- Python 
- Django 
- Django REST Framework
- PostgreSQL

### Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:
    ```bash
    - git@github.com:belikrastr/api_yamdb.git
    ```
    ```bash
    - cd api_yamdb
    ```
- Cоздать и активировать виртуальное окружение:
    ```bash
    - python -m venv env
    ```
    ```bash
    - source env/Scripts/activate
    ```
    ```bash
    - python -m pip install --upgrade pip
    ```
- Установить зависимости из файла requirements.txt:
    ```bash
    - pip install -r requirements.txt
    ```
- Перейти в директорию yatube:
    ```bash
    - cd api_yamdb
    ```
- Выполнить миграции:
    ```bash
    - python manage.py migrate
    ```
- Запустить проект:
    ```bash
    - python manage.py runserver
    ```
### Примеры запросов for Users:

- Регистрация пользователя и получение confirmation_code
###
POST http://127.0.0.1:8000/api/v1/auth/signup/
Content-Type: application/json
```js
{
    "email": "user@mail.ru",
    "username": "user"
}
```

- Получение токена пользователя
###
POST http://127.0.0.1:8000/api/v1/auth/token/
Content-Type: application/json
```js
{
    "username": "user2",
    "confirmation_code": "65y-64a6e988500b2eeac0b"
}
```
- Получить данные своей учетной записи
###
GET  http://127.0.0.1:8000/api/v1/users/me/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4OTQ4Njc1LCJqdGkiOiJjYmE4NGMzZGUzYjI0ODA5OTY3ZjJiODZiOTM2YjQzYiIsInVzZXJfaWQiOjV9.guSbTtW-YBKsmOYzwzE7xu0tPXQ7dMoI2YzbAi4ZSw8


- Изменить данные своей учетной записи
###
PATCH http://127.0.0.1:8000/api/v1/users/me/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4ODA0ODU3LCJqdGkiOiIyZjEzZWMzZWM1MDU0ODI0OTU1ZmUwM2Y4MmE2NDU2NSIsInVzZXJfaWQiOjV9.bzQTBMpOjztnhLwo-rXGQXY7eqwzyX23XtqkMq0f22U
Content-Type: application/json
```js
{
    "username": "user2",
    "email": "user2@mail.ru",
    "first_name": "User",
    "last_name": "user",
    "bio": "",
    "role": "user"
}
```

- Получение списка всех пользователей с токеном Админа
###
GET   http://127.0.0.1:8000/api/v1/users/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4ODc3NTUzLCJqdGkiOiJmOGI5NDNhMjY5Mjk0MWNkOGQzZmQyYzk4N2JlODljOSIsInVzZXJfaWQiOjJ9.rw69vzp1RU80K-2PHiGPjRVm3umj0cKCaAy5ulZ7xJc
Content-Type: application/json


- Получаем token admin
###
POST http://127.0.0.1:8000/api/v1/auth/token/
Content-Type: application/json
```js
{
    "username": "admin"
}
```
### Автор проекта
Беликов Владимир - [Telegram](https://t.me/belikrastr) - belikrastr@yandex.ru

Project Link: [https://github.com/belikrastr/api_yamdb](https://github.com/belikrastr/api_yamdb)
