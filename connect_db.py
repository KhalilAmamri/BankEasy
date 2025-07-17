import psycopg2
try:
    conn = psycopg2.connect(
        dbname='bank_app',
        user='postgres',
        password='PostgreSQLKhalil',
        host='localhost',
        port='5432'
    )
    print("Database connection successful")
    conn.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")