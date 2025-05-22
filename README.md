# FSTR pereval REST API

Проект FSTR_pereval предоставляет API для работы с информацией о горных перевалах. Это API включает возможности добавления, редактирования, удаления и просмотра информации о различных перевалах.

Установка проекта:
```
git clone https://github.com/aQu4123/FSTR_pereval.git
cd FSTR_pereval
```
Создание виртуального окружения:
```
python -venv .venv
```
Установка зависимостей:
```
pip install -r requirements.txt
```
Подключите(создайте) базу данных PostgresSQL и создайте файл .env в корневой директории проекта(на одном уровне manage.py) и заполните его следующими данными:
```
FSTR_DB_NAME=your_db_name  # имя БД
FSTR_DB_LOGIN=your_db_user  # имя пользователя
FSTR_DB_PASS=your_db_password  # пароль
FSTR_DB_HOST=localhost
FSTR_DB_PORT=port # Обычно порт для PostgreSQL — 5432
```
После примените миграции:
```
python .\manage.py migrate
```
Запуск сервера проекта:
```
python .\manage.py runserver
```
Документация с помощью Swagger:
```
http://127.0.0.1:8000/swagger
```
Основные эндпоинты

POST   `/api/submitData/` - Добавить новый перевал

GET    `/api/submitData/?user__email=example@mail.ru` - Получить список перевалов по email 

GET    `/api/submitData/<id>/` -  Получить информацию о перевале по ID 

PATCH  `/api/submitData/<id>/` - Обновить перевал (если status = "new") 

Пример POST-запроса

```json
{
    "user": {
        "email": "qwerty@mail.ru",
        "phone": "+7 555 55 55",
        "fam": "Пупкин",
        "name": "Василий",
        "otc": "Иванович"
    },
    "coords": {
        "latitude": 45.3842,
        "longitude": 7.1525,
        "height": 1200.0
    },
    "level": {
        "winter": "",
        "summer": "1А",
        "autumn": "1А",
        "spring": ""
    },
    "beautyTitle": "пер.",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "",
    "add_time": "2025-05-21 12:56:17",
    "images": [
        {
            "data": "http://example.com/image1.jpg",
            "title": "Седловина"
        },
        {
            "data": "http://example.com/image2.jpg",
            "title": "Подъем"
        }
    ]
}
```

Проект выполнен в рамках учебного задания школы Skillfactory для Федерации спортивного туризма России (ФСТР).
