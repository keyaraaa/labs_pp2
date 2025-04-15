import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="keyara",
    password=""
)

cur = conn.cursor()

name = input("Введите имя: ")
phone = input("Введите номер телефона: ")

cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))

conn.commit()
print("Данные успешно добавлены!")

cur.close()
conn.close()