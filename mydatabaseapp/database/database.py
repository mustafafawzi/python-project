import sqlite3
import os

class Database:
    def __init__(self, db_path):
        print("Attempting to connect to database at:", db_path)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        print("Connection successful!")

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_all(self, table):
        query = f"SELECT * FROM {table}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def insert_user(self, name, email):
        query = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')"
        self.execute_query(query)

    def update_user_email(self, user_id, new_email):
        query = f"UPDATE users SET email = '{new_email}' WHERE id = {user_id}"
        self.execute_query(query)

    def delete_user(self, user_id):
        query = f"DELETE FROM users WHERE id = {user_id}"
        self.execute_query(query)

    def fetch_orders_by_user(self, user_id):
        query = f"SELECT * FROM orders WHERE user_id = {user_id}"
        self.cursor.execute(query)
        orders = self.cursor.fetchall()
        return orders

    def get_table_names(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        self.cursor.execute(query)
        tables = self.cursor.fetchall()
        return [table[0] for table in tables]

    def execute_custom_query(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            return f"Error executing query: {e}"
