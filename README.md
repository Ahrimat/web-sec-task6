# Library MVC (Flask) — Практическая работа №6
Минимальное веб-приложение библиотеки с архитектурой, близкой к MVC (Model-View-Controller) на Python (Flask + SQLAlchemy).

## Структура проекта
- app.py — точка входа, настройка Flask и маршрутов
- models.py — SQLAlchemy модели + инициализация БД
- controllers/book_controller.py — маршруты/контроллеры для сущности Book
- templates/ — Jinja2 шаблоны (views)
  - base.html, books_list.html, book_detail.html, book_form.html, confirm_delete.html
- static/css/style.css — минимальные стили
- requirements.txt — зависимости
- init_db.py — скрипт для инициализации БД с тестовыми данными
- architecture.md — краткое описание архитектуры + диаграмма (ASCII)

## Запуск
1. Создайте виртуальное окружение (рекомендуется):
   python -m venv venv
   source venv/bin/activate 
2. Установите зависимости:
   pip install -r requirements.txt
3. Инициализируйте БД (создаст файл library.db и заполнит примерами):
   python init_db.py
4. Запустите приложение:
   flask run
   Или:
   python app.py
5. Перейдите в браузере: http://127.0.0.1:5000/books

## Описание
Сущность: Book (id, title, author, year, isbn, description).
Поддерживается CRUD: список, просмотр, создание, редактирование, удаление.
Поиск по названию/автору через параметр ?q=...

## Замечания по архитектуре
- Model: models.py (SQLAlchemy)
- Controller: controllers/book_controller.py (Flask Blueprints / маршруты)
- View: templates/ (Jinja2)
- Файловая структура отделяет слои и легко расширяется.
