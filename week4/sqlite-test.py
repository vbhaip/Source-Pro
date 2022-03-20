import sqlite3
import random

conn = sqlite3.connect('temp.db')

conn.execute('CREATE TABLE people (first_name TEXT, last_name TEXT, age INTEGER, phone_number INTEGER)')

# https://stackoverflow.com/questions/305378/list-of-tables-db-schema-dump-etc-using-the-python-sqlite3-api

conn.execute("INSERT INTO people VALUES (?,?,?,?)", ("Vinay", "Bhaip", 20, 1234567890))
conn.commit()

first_names = ["Tony", "Steve", "Bruce"]
last_names = ["Stark", "Rogers", "Banner"]


for i in range(0, 1000):
    conn.execute("INSERT INTO people VALUES (?,?,?,?)", (random.choice(first_names), 
    random.choice(last_names), random.randint(15, 50), random.randint(1000000000, 9999999999)))

conn.commit()


result = conn.execute("SELECT * from people WHERE first_name LIKE '%e' ")
conn.commit()

print(result.fetchall())