import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname='bank_app',
        user='postgres',
        password='PostgreSQLKhalil',
        host='localhost',
        port='5432'
    )