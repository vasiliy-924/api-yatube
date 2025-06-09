# Yatube API

REST API для социальной сети Yatube, разработанное с использованием Django REST Framework.

## Описание

Yatube API предоставляет интерфейс для взаимодействия с социальной сетью Yatube. API позволяет создавать, читать, обновлять и удалять посты, комментарии, а также управлять подписками на авторов.

## Технологии

- Python 3.7+
- Django 5.1.1
- Django REST Framework 3.15.2
- SQLite3

## Установка

1. Клонируйте репозиторий:
```bash
git clone git@github.com:vasiliy-924/api-yatube.git
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Запустите сервер разработки:
```bash
python manage.py runserver
```

## API Endpoints

- `/api/v1/posts/` - управление постами
- `/api/v1/posts/{post_id}/comments/` - управление комментариями
- `/api/v1/follow/` - управление подписками
- `/api/v1/groups/` - управление группами

## Тестирование

Для запуска тестов используйте:
```bash
pytest
```

## Лицензия

MIT
