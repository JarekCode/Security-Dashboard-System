import psycopg2, os
from dotenv import load_dotenv

class DBController():
    def test_operation():
        load_dotenv("./.env")
        db_connect = psycopg2.connect(database=str(os.getenv('DB_NAME')), host=str(os.getenv('DB_HOST')), user=str(os.getenv('DB_USER')), password=str(os.getenv('DB_PASSWORD')), port=int(os.getenv('DB_PORT')), options=f"-c search_path={str(os.getenv('DB_SCHEMA_ADMIN'))}")
        db_cursor = db_connect.cursor()

        db_cursor.execute("""
                        CREATE TABLE IF NOT EXISTS person (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255),
                        age INT
                        );
        """)

        db_cursor.execute("""
                        INSERT INTO person (name, age) VALUES
                        ('Test Name', 100);
        """)

        # Commit & Close DB
        db_connect.commit()
        db_cursor.close()
        db_connect.close()