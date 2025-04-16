import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",  # если хочешь — можешь создать отдельную базу
    user="keyara",
    password=""
)

cur = conn.cursor()

username = input("Введите имя пользователя: ")

# Проверяем, существует ли пользователь
cur.execute("SELECT id, level FROM game_user WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id, level = user
    print(f"Добро пожаловать обратно, {username}! Ваш текущий уровень: {level}")
else:
    # Создаём нового пользователя
    cur.execute("INSERT INTO game_user (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    level = 1
    print(f"Новый пользователь {username} успешно зарегистрирован. Уровень: {level}")

conn.commit()
cur.close()
conn.close()