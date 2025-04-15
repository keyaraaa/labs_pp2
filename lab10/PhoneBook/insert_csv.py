import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="keyara",
    password=""
)

cur = conn.cursor()

with open('contacts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # пропускаем заголовок, если он есть
    for row in reader:
        name, phone = row
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))

conn.commit()
print("Данные из CSV успешно добавлены!")

cur.close()
conn.close()