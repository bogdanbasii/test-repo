import sqlite3

db = sqlite3.connect('database.sqlite')

cursor = db.cursor()

query = "INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)"

records = [
    ("Peter", "Frampton", 32),
    ("John", "Peterson", 43),
    ("Mike", "Johnson", 56),
    ("Joe", "Michaelson", 45),
    ("Gill", "Mill", 20)
]


cursor.executemany(query, records)

db.commit()

cursor.close()
db.close()