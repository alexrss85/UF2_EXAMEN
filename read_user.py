import psycopg2 as psy
from connection import conexio

# EXERCICI 4
def readUsers(conn):
    connection = conn.cursor()
    connection.execute("select * from users;")
    conn.commit()
    users=connection.fetchall()
    return users