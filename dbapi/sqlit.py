import sqlite3


conn = sqlite3.connect(
    database="mytest_db.sqlite3",
)

cur = conn.cursor()


stmt = """
create table if not exists users (
    id integer primary key,
    email text not null,
    password text not null
)
"""

cur.execute(stmt)
conn.commit()


cur.close()
conn.close()