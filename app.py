from flask import Flask, redirect
from models import db, init_db
from controllers.book_controller import books_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-key'
    db.init_app(app)

    app.register_blueprint(books_bp)

    @app.route('/')
    def index():
        return redirect('/books')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        init_db()
    app.run(debug=True)
