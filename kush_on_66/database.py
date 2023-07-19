```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    conn.close()

def execute_query(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)

def create_tables(conn):
    user_table_query = """ CREATE TABLE IF NOT EXISTS users (
                                        user_id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL,
                                        email text NOT NULL,
                                        preferences text
                                    ); """

    product_table_query = """CREATE TABLE IF NOT EXISTS products (
                                    product_id integer PRIMARY KEY,
                                    product_name text NOT NULL,
                                    product_type text NOT NULL,
                                    product_description text NOT NULL,
                                    product_price real NOT NULL
                                );"""

    review_table_query = """CREATE TABLE IF NOT EXISTS reviews (
                                    review_id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    product_id integer NOT NULL,
                                    review_text text NOT NULL,
                                    review_rating integer NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (user_id),
                                    FOREIGN KEY (product_id) REFERENCES products (product_id)
                                );"""

    order_table_query = """CREATE TABLE IF NOT EXISTS orders (
                                    order_id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    product_id integer NOT NULL,
                                    order_quantity integer NOT NULL,
                                    order_status text NOT NULL,
                                    order_type text NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (user_id),
                                    FOREIGN KEY (product_id) REFERENCES products (product_id)
                                );"""

    execute_query(conn, user_table_query)
    execute_query(conn, product_table_query)
    execute_query(conn, review_table_query)
    execute_query(conn, order_table_query)

def main():
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```