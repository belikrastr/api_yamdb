# Проект YaMDb
### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

### Технологии
- Python 
- Django 
- Django REST Framework
- Nginx
- Docker
- Postgresql
- JWT Token

### Подготовка к запуску проекта
- Склонировуйте репозиторий на локальную мшину
```bash
git git@github.com:belikrastr/api_yamdb.git
```
- Перейдите в директорию api_yamdb
```bash
cd api_yamdb
```

- Cоздайте .env файл в директории и впишите:
```python
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Запуск проекта 
- Запустите docker-compose:
```bash
docker-compose up -d --build
```
```bash
docker-compose up
```
- Выполните миграции:
```bash
docker-compose exec backend python manage.py migrate
```
- Создайте суперпользователя:
```bash
docker-compose exec backend python manage.py createsuperuser
```
- Соберите статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input
```
### Примеры запросов к API.

- Регистрация пользователя и получение confirmation_code
###
POST http://localhost/api/v1/auth/signup/
Content-Type: application/json
```js
{
    "email": "user@mail.ru",
    "username": "user"
}
```

- Получение токена пользователя
###
POST http://localhost/api/v1/auth/token/
Content-Type: application/json
```js
{
    "username": "user2",
    "confirmation_code": "65y-64a6e988500b2eeac0b"
}
```
- Получить данные своей учетной записи
###
GET  http://localhost/api/v1/users/me/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4OTQ4Njc1LCJqdGkiOiJjYmE4NGMzZGUzYjI0ODA5OTY3ZjJiODZiOTM2YjQzYiIsInVzZXJfaWQiOjV9.guSbTtW-YBKsmOYzwzE7xu0tPXQ7dMoI2YzbAi4ZSw8


- Изменить данные своей учетной записи
###
PATCH http://localhost/api/v1/users/me/
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
GET   http://localhost/api/v1/users/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4ODc3NTUzLCJqdGkiOiJmOGI5NDNhMjY5Mjk0MWNkOGQzZmQyYzk4N2JlODljOSIsInVzZXJfaWQiOjJ9.rw69vzp1RU80K-2PHiGPjRVm3umj0cKCaAy5ulZ7xJc
Content-Type: application/json


- Получаем token admin
###
POST http://localhost/api/v1/auth/token/
Content-Type: application/json
```js
{
    "username": "admin"
}
```
### Авторы проекта
supersushichi
Беликов Владимир - [Telegram](https://t.me/belikrastr) - belikrastr@yandex.ru

Project Link: [https://github.com/belikrastr/api_yamdb](https://github.com/belikrastr/api_yamdb)
