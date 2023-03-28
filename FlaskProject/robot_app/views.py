from flask import request, render_template, redirect, abort

from robot_app import app
import random
@app.route('/hello')
def hello_world():
    app.logger.info("This is a request to '/hello")
    return 'Hello World!'

names = ['Ivan', 'Petro', 'Mykola', 'Vasyl', 'Oleksandr', 'Anton']
books = ['Kobzar', 'Bible', 'Quran', 'Eneida', 'Odyssey']

@app.get('/users')
def rand_user():
    random_names = random.sample(names, random.randint(1, len(names)))
    return ', '.join(random_names)

@app.get('/books')
def rand_books():
    random_books = random.sample(books, random.randint(1, len(books)))
    book_list = '<ul>'
    for book in random_books:
        book_list += f'<li>{book}</li>'
    book_list += '</ul>'
    return book_list

@app.get('/users/<int:id>')
def get_user(id):
    if id % 2 == 0:
        return f"User ID: {id}", 200
    else:
        return "Not Found", 404

@app.get('/books/<string:title>')
def get_book(title):
    converted_title = title.capitalize()
    return converted_title

@app.get('/params')
def get_params():
    query_params = request.args.to_dict()
    table = "<table><tr><th>parameter</th><th>value</th></tr>"
    for key, value in query_params.items():
        table += f"<tr><td>{key}</td><td>{value}</td></tr>"
    table += "</table>"
    return table, 200

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        html_form = """
                <form method="POST" action="/login">
                    <table>
                        <tr>
                            <td><label for="username">Username:</label></td>
                            <td><input type="text" id="username" name="username" value=""></td>
                        </tr>
                        <tr>
                            <td><label for="password">Password:</label></td>
                            <td><input type="password" id="password" name="password" value=""></td>
                        </tr>
                    </table>
                    <button type="submit">Submit</button>
                </form>
                """
        return html_form, 200
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect('/users')
        else:
            abort(400, 'Missing username or password')