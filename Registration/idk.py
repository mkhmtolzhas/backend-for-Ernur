import sqlite3
import json

# Открываем соединение с базой данных SQLite
conn = sqlite3.connect('B:/VS CODE/backend/DataBase/user_data.db')
cursor = conn.cursor()

# Читаем данные из JSON-файла
with open('B:/VS CODE/backend/Registration/user.json', 'r') as file:
    data = json.load(file)

# Пример схемы таблицы в базе данных SQLite
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT)''')

# Проходимся по данным из JSON-файла и вставляем их в базу данных
# for user in data:
cursor.execute('''INSERT INTO users (first_name, last_name, email)
                VALUES (?, ?, ?)''', (data['first_name'], data['second_name'], data['email']))

# Сохраняем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()
