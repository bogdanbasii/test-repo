from flask import request, render_template, redirect, abort, session

from robot_app import app
import random

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
def rand_user():
    if 'username' in session:
        username = session['username']
        random_names = random.sample(names, random.randint(1, len(names)))
        return render_template('users.html', names=random_names, username=username)
    else:
        return redirect('/login')

@app.get('/books')
def rand_books():
    random_books = random.sample(books, random.randint(1, len(books)))
    book_list = '<ul>'
    for book in random_books:
        book_list += f'<li>{book}</li>'
    book_list += '</ul>'
    return render_template('books.html', book_list=book_list)

@app.get('/users/<int:id>')
def get_user(id):
    if id % 2 == 0:
        is_found = True
    else:
        is_found = False
    return render_template('users_id.html', id=id, is_found=is_found)

@app.get('/books/<string:title>')
def get_book(title):
    converted_title = title.capitalize()
    return render_template('book_title.html', title=converted_title)

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
