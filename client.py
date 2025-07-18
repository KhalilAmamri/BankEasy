from connect_db import get_connection

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def get_all():
        conn = get_connection()
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT client_id, name, email FROM clients")
                return cursor.fetchall()

    def add_to_db(self):
        conn = get_connection()
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO clients (name, email) VALUES (%s, %s) RETURNING client_id",
                    (self.name, self.email)
                )
                client_id = cursor.fetchone()[0]
                print(f"New client added with ID: {client_id}")
                return client_id