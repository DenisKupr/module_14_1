import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(1, 11):
#     cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

# cursor.execute("UPDATE Users SET balance = 500 WHERE id in (1, 3, 5, 7, 9)")

# cursor.execute("DELETE FROM Users WHERE id in (1, 4, 7, 10)")

cursor.execute("SELECT Username, email, age, balance FROM Users WHERE age !=60")
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]}", f" | Почта: {user[1]}", f" | Возраст: {user[2]}", f" | Баланс: {user[3]}")

connection.commit()
connection.close()