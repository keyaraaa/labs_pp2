import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="keyara",
    password=""
)

cur = conn.cursor()

filter_value = input("Введите имя или номер для поиска: ")

cur.execute("SELECT * FROM contacts WHERE name = %s OR phone = %s", (filter_value, filter_value))
results = cur.fetchall()

if not results:
    print("Ничего не найдено.")
else:
    for row in results:
        print(row)

cur.close()
conn.close()
