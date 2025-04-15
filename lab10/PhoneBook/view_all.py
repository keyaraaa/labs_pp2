import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="keyara",
    password=""
)

cur = conn.cursor()

cur.execute("SELECT * FROM contacts")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()