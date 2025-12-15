import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mytest_db",
    user="postgres",
    password="voidpostgres"
) # TCP connection


# Open a cursor to perform database operations
cur = conn.cursor()


def create_table(cur):
    stmt = """
    CREATE TABLE IF NOT EXISTS
        users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            is_active BOOLEAN DEFAULT true
        );
    """

    cur.execute(stmt)
    conn.commit()


def insert_data(cur):
    stmt = """
    INSERT INTO users (email, password)
    VALUES (%s, %s)
    RETURNING id;
    """
    
    email = input("Enter email: ")
    password = input("Enter password: ")

    cur.execute(stmt, (email, password))
    conn.commit()
    

def select_users(cur):
    stmt = """
    SELECT * from users;
    """

    cur.execute(stmt)
    return cur.fetchall()


create_table(cur)
insert_data(cur)
print(select_users(cur))

conn.close()