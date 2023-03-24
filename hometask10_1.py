import sqlite3

db = sqlite3.connect('database.sqlite')

cursor = db.cursor()

query = "CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, age INTEGER)"
cursor.execute(query)

db.commit()