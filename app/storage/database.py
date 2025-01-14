import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    try: 
        connection = psycopg2.connect(host="localhost", database="docker", user="--USERNAME--", password="--Password--", port="5432", cursor_factory=RealDictCursor)
        cur = connection.cursor()
        print(f"Database connected")
        cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'todo'
            );
        """)
        table_exists = cur.fetchone()
        print(f"table exists: {table_exists}")
        if not table_exists["exists"]:
            cur.execute("""
                CREATE TABLE todo (
                    id SERIAL PRIMARY KEY,
                    task VARCHAR(255) NOT NULL
                );
            """)
            print("Table 'todo' created successfully.")
        else:
            print("Table 'todo' already exists.")
        connection.commit()
        cur.close()
        return connection
    except Exception as error:
        print(f"Couldn't connect to database the error occured was {error}")
        return None


def create_task(task:str):
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("""INSERT INTO todo (task) VALUES (%s) RETURNING *;""", (task,))
            new_task = cur.fetchone()
            conn.commit()
            return new_task
        except Exception as error:
            print(f"Couldn't add new task to the database, following  error {error} occured.")
            return None
        finally:
            cur.close()
            conn.close()


def delete_task_db(id:int):
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("""DELETE FROM todo WHERE id=%s RETURNING *;""", (str(id), ))
            deleted_task = cur.fetchone()
            conn.commit()
            return deleted_task
        except Exception as error:
            print(f"Couldn't delete task with id {id}, following error occured: {error}")
            return None
        finally:
            cur.close()
            conn.close()



