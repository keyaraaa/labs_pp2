import psycopg2
from datetime import datetime

# Данные игрока, которые получаешь из игры
username = input("Введите имя пользователя: ")
score = int(input("Введите текущий счёт: "))
level = int(input("Введите текущий уровень: "))

# Подключение к базе
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="keyara",
    password=""
)
cur = conn.cursor()

# Получаем ID игрока
cur.execute("SELECT id FROM game_user WHERE username = %s", (username,))
result = cur.fetchone()

if result:
    user_id = result[0]

    # Обновляем уровень игрока
    cur.execute("UPDATE game_user SET level = %s WHERE id = %s", (level, user_id))

    # Добавляем очки в таблицу user_score
    cur.execute(
        "INSERT INTO user_score (user_id, score, timestamp) VALUES (%s, %s, %s)",
        (user_id, score, datetime.now())
    )

    conn.commit()
    print(f"Счёт ({score}) и уровень ({level}) успешно сохранены!")
else:
    print("Пользователь не найден!")

cur.close()
conn.close()