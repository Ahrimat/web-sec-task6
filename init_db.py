from app import create_app
from models import db, Book
import os

app = create_app()
db_path = os.path.join(os.path.dirname(__file__), 'library.db')
with app.app_context():
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
        except Exception:
            pass
    db.create_all()
    samples = [
        Book(title='Преступление и наказание', author='Федор Достоевский', year=1866, isbn='978-0140449136', description='Психологическая новелла.'),
        Book(title='Война и мир', author='Лев Толстой', year=1869, isbn='978-0199232765', description='Крутая новела.'),
        Book(title='Капитанская дочка', author='Александр Пушкин', year=1951, isbn='978-0316769488', description='Просто крутая книга.'),
        Book(title='Дубровский', author='Александр Пушкин', year=1951, isbn='978-0316769488', description='Книга о хорошем человеке.'),
    ]
    for s in samples:
        db.session.add(s)
    db.session.commit()
    print('Initialized database with sample data.')
