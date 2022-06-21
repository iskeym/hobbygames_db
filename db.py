import sqlite3

conn = sqlite3.connect('myDataBase.db')

sql = "CREATE TABLE games (title TEXT, price TEXT, article TEXT, availability TEXT, link TEXT)"
cursor = conn.cursor()

conn.close()