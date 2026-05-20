import sqlite3

connection = sqlite3.connect("app.db")

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """
)

connection.commit()
connection.close()
