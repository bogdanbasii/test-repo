from flask import request, render_template, redirect, abort, session, jsonify
from .models import *
from robot_app import app

@app.before_request
def before_request():
    if not session.get('username') and request.endpoint != 'login':
        return redirect('/login')


@app.route('/hello')
def hello_world():
    app.logger.info("This is a request to '/hello")
    return 'Hello World!'

names = ['Ivan', 'Petro', 'Mykola', 'Vasyl', 'Oleksandr', 'Anton']
books = ['Kobzar', 'Bible', 'Quran', 'Eneida', 'Odyssey']

@app.get('/users')
def get_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'age': user.age} for user in users]
    return jsonify(users_list)

@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'age': user.age}
        return jsonify(user_data)
    else:
        abort(404, f'User with id {user_id} not found')


@app.get('/books')
def get_books():
    books = Book.query.all()
    books_list = [{'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year, 'price': book.price} for book in books]
    return jsonify(books_list)

@app.get('/books/<int:book_id>')
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book_data = {'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year, 'price': book.price}
        return jsonify(book_data)
    else:
        abort(404, f'Book with id {book_id} not found')

@app.get('/purchases')
def get_purchases():
    purchases = Purchase.query.all()
    purchases_list = [{'id': purchase.id, 'user_id': purchase.user_id, 'book_id': purchase.book_id, 'date': purchase.date} for purchase in purchases]
    return jsonify(purchases_list)

@app.get('/purchases/<int:purchase_id>')
def get_purchase(purchase_id):
    purchase = Purchase.query.get(purchase_id)
    if purchase:
        purchase_data = {'id': purchase.id, 'user_id': purchase.user_id, 'book_id': purchase.book_id, 'date': purchase.date}
        return jsonify(purchase_data)
    else:
        abort(404, f'Purchase with id {purchase_id} not found')

@app.get('/params')
def get_params():
    query_params = request.args.to_dict()
    table_data = []
    for key, value in query_params.items():
        table_data.append({'param': key, 'value': value})
    return render_template('params.html', table_data=table_data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            session['username'] = username
            return redirect('/users')
        else:
            abort(400, 'Missing username or password')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')
