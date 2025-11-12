from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Book

books_bp = Blueprint('books', __name__, template_folder='../templates')

def validate_book_form(form):
    errors = {}
    title = form.get('title','').strip()
    author = form.get('author','').strip()
    year = form.get('year','').strip()
    if not title:
        errors['title'] = 'Название обязательно.'
    if not author:
        errors['author'] = 'Автор обязателен.'
    if year:
        try:
            y = int(year)
            if y < 0 or y > 2025:
                errors['year'] = 'Невалидная дата.'
        except ValueError:
            errors['year'] = 'Год должен быть числом.'
    return errors

@books_bp.route('/books')
def list_books():
    q = request.args.get('q','').strip()
    if q:
        books = Book.query.filter((Book.title.contains(q)) | (Book.author.contains(q))).all()
    else:
        books = Book.query.order_by(Book.id.desc()).all()
    return render_template('books_list.html', books=books, q=q)

@books_bp.route('/books/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book=book)

@books_bp.route('/books/create', methods=['GET','POST'])
def create_book():
    if request.method == 'POST':
        form = request.form
        errors = validate_book_form(form)
        if errors:
            return render_template('book_form.html', form=form, errors=errors, action='Create')
        book = Book(
            title=form.get('title').strip(),
            author=form.get('author').strip(),
            year=int(form.get('year')) if form.get('year') else None,
            isbn=form.get('isbn').strip() or None,
            description=form.get('description').strip() or None
        )
        db.session.add(book)
        db.session.commit()
        flash('Book created successfully.')
        return redirect(url_for('books.list_books'))
    return render_template('book_form.html', form={}, errors={}, action='Create')

@books_bp.route('/books/edit/<int:book_id>', methods=['GET','POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        form = request.form
        errors = validate_book_form(form)
        if errors:
            return render_template('book_form.html', form=form, errors=errors, action='Edit', book=book)
        book.title = form.get('title').strip()
        book.author = form.get('author').strip()
        book.year = int(form.get('year')) if form.get('year') else None
        book.isbn = form.get('isbn').strip() or None
        book.description = form.get('description').strip() or None
        db.session.commit()
        flash('Book updated successfully.')
        return redirect(url_for('books.book_detail', book_id=book.id))
    form = {
        'title': book.title,
        'author': book.author,
        'year': book.year or '',
        'isbn': book.isbn or '',
        'description': book.description or ''
    }
    return render_template('book_form.html', form=form, errors={}, action='Edit', book=book)

@books_bp.route('/books/delete/<int:book_id>', methods=['GET','POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted.')
        return redirect(url_for('books.list_books'))
    return render_template('confirm_delete.html', book=book)
