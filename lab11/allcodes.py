import psycopg2

# Подключение к базе данных
def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="keyara",
        password=""
    )

# Создание таблицы
def create_contacts_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

# Поиск по шаблону
def search_contacts(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM contacts
        WHERE name ILIKE %s OR phone ILIKE %s
    """, (f"%{pattern}%", f"%{pattern}%"))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

# Вставка или обновление одного контакта
def insert_or_update_user(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name = %s", (name,))
    if cur.fetchone():
        cur.execute("UPDATE contacts SET phone = %s WHERE name = %s", (phone, name))
    else:
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

# Массовая вставка

def insert_many(users):
    conn = connect()
    cur = conn.cursor()
    invalid = []
    for name, phone in users:
        if len(phone) == 11 and phone.isdigit():
            cur.execute("SELECT * FROM contacts WHERE name = %s", (name,))
            if cur.fetchone():
                cur.execute("UPDATE contacts SET phone = %s WHERE name = %s", (phone, name))
            else:
                cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
        else:
            invalid.append((name, phone))
    conn.commit()
    cur.close()
    conn.close()
    return invalid

# Пагинация
def get_paginated_contacts(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

# Удаление по имени или номеру
def delete_contact(value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    cur.close()
    conn.close()

# Меню
if __name__ == "__main__":
    create_contacts_table()

    while True:
        print("""
==== PHONEBOOK МЕНЮ ====
1. Поиск по шаблону
2. Вставить или обновить контакт
3. Массовая вставка
4. Показать с пагинацией
5. Удалить по имени или номеру
0. Выход
========================
        """)
        choice = input("Выбери опцию: ")

        if choice == "1":
            pattern = input("Введите шаблон для поиска: ")
            for row in search_contacts(pattern):
                print(row)

        elif choice == "2":
            name = input("Имя: ")
            phone = input("Телефон: ")
            insert_or_update_user(name, phone)
            print("Контакт добавлен или обновлён")

        elif choice == "3":
            n = int(input("Сколько контактов ввести? "))
            users = []
            for _ in range(n):
                name = input("Имя: ")
                phone = input("Телефон: ")
                users.append((name, phone))
            invalid = insert_many(users)
            print("Некорректные контакты:", invalid)

        elif choice == "4":
            limit = int(input("Сколько показать? "))
            offset = int(input("Пропустить сколько? "))
            for row in get_paginated_contacts(limit, offset):
                print(row)

        elif choice == "5":
            val = input("Имя или номер: ")
            delete_contact(val)
            print("Контакт удалён, если был найден")

        elif choice == "0":
            break

        else:
            print("Неверный ввод. Попробуй снова.")