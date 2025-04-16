import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",  # или другую базу, если хочешь отдельно
    user="keyara",
    password=""
)

cur = conn.cursor()

# Таблица пользователей
cur.execute("""
CREATE TABLE IF NOT EXISTS game_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    level INTEGER DEFAULT 1
);
""")

# Таблица счёта
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES game_user(id),
    score INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
print("Таблицы для Snake Game успешно созданы!")

cur.close()
conn.close()