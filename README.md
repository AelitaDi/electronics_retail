# Electronic retail

Проект модели сети продажи электроники.
***

## Установка и запуск

### 1. Требования

- Python 3.11+

- PostgreSQL

- Установленные зависимости из  `requirements.txt`

### 2. Клонируйте репозиторий:

```
git clone https://github.com/AelitaDi/electronics_retail
cd electronics_retail
```

### 3. Установите виртуальное окружение

1. Создайте виртуальное окружение:
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

### 4. Подключите БД

1. Создайте файл **.env** и заполните его по образцу **.env.sample**:
   ```
   SECRET_KEY=django-insecure-12345!abcde67890!@#qwerty
   DATABASE_NAME=<db_name>
   DATABASE_USER=<user>
   DATABASE_PASSWORD=<your_password>
   DATABASE_HOST=localhost
   DATABASE_PORT=5432

   ```
2. Примените миграции:
   ```
   python manage.py migrate
   ```

3. Создайте суперпользователя:
   ```
   python manage.py csu
   ```
   username: admin@example.com
   password: admin

4. Запустите проект:
   ```
   python manage.py runserver
   ```
5. Используйте административную панель Django (`http://127.0.0.1:8000/admin/`) для добавления:
    - Пользователей 
    - Продуктов
    - Звеньев сети
    - Контактов для звеньев сети
   
   Также через админ-панель (admin-action) можно обнулять задолженность звена перед поставщиком.

## Использование API

Ознакомиться можно здесь:`http://127.0.0.1:8000/swagger/`
Через API можно регистрировать и залогинивать пользователей, создавать звенья сети, просматривать и редактировать
информацию о звеньях сети.

## Авторы

[Rogova U.](https://github.com/AelitaDi)