import sqlite3


def initiate_db(db_path="database.db"):
    """Функция для инициализации базы данных и создания таблицы Products."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    create_table_query = """CREATE TABLE IF NOT EXISTS Products ( id INTEGER PRIMARY KEY, title TEXT NOT NULL, description TEXT, 
    price INTEGER NOT NULL );"""

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()


def get_all_products(db_path="database.db"):
    """Функция для получения всех записей из таблицы Products."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    select_query = "SELECT * FROM Products;"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    conn.close()
    return rows


def add_product(title, description, price, db_path="database.db"):
    """Функция для добавления нового продукта в таблицу Products."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    insert_query = f""" INSERT INTO Products (title, description, price) VALUES ('{title}', '{description}', {price}); """

    cursor.execute(insert_query)
    conn.commit()
    conn.close()
