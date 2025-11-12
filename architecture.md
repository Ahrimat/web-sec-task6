# Архитектура приложения — Library MVC (Flask)

Приложение разделено на слои в духе MVC:

- Model (models.py)
  - SQLAlchemy модель Book
  - Инициализация БД (db)
- Controller (controllers/book_controller.py)
  - Flask Blueprint `books_bp`
  - Все маршруты CRUD и логика валидации форм
- View (templates/*.html)
  - Jinja2 шаблоны: base.html, books_list.html, book_detail.html, book_form.html, confirm_delete.html

Простейшая схема (ASCII):

Пользователь (браузер)
       ↓
Routes / Controllers (Flask Blueprints)
       ↓
Models / DB (SQLAlchemy + SQLite)
       ↑
Views (Jinja2 templates) ←─ Rendered HTML
