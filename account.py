from connect_db import get_connection

class Account:
    def __init__(self, name, balance, client_id):
        self.name = name
        self.balance = balance
        self.client_id = client_id

    @staticmethod
    def get_all():
        conn = get_connection()
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT account_id, name, balance, client_id FROM accounts")
                return cursor.fetchall()

    def add_to_db(self):
        conn = get_connection()
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO accounts (name, balance, client_id) VALUES (%s, %s, %s) RETURNING account_id",
                    (self.name, self.balance, self.client_id)
                )
                account_id = cursor.fetchone()[0]
                print(f"New account added with ID: {account_id}")
                return account_id