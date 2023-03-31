from flask.views import View, MethodView
from flask import request
from robot_app import app
class MyViews(View):
    methods = ['GET', 'POST']
    def __init__(self, data, template_name):
        self.data = data
        self.template = template_name


    def dispatch_request(self):
        if request.method == 'GET':
            return f"Data: {self.data}, template_name: {self.template}", 200
        else:
            return 'ok', 201

class MyMethodView(MethodView):

    def get(self):
        return 'Method GET ok', 200
    def post(self):
        return 'Method POST ok', 201

users = ['First', 'Second', 'Third']
books = ['Kobzar', 'Harry Potter', 'Lisova Pisnia']
movies = ['Avengers', 'Sherlock Holmes']

app.add_url_rule('/class/users', view_func=MyViews.as_view('users', users, 'users.html'))

app.add_url_rule('/class/books', view_func=MyViews.as_view('books', books, 'books.html'))

app.add_url_rule('/class/movies', view_func=MyViews.as_view('movies', movies, 'movies.html'))

app.add_url_rule('/class/methods', view_func=MyMethodView.as_view('class-methods'))