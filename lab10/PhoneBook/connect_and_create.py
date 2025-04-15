import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",     # Название твоей базы
    user="keyara",            # Замени на своё имя пользователя macOS
    password=""               # Если нет пароля, оставь пустым
)

cur = conn.cursor()

# Создание таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    );
""")

conn.commit()
print("Таблица contacts успешно создана!")

cur.close()
conn.close()