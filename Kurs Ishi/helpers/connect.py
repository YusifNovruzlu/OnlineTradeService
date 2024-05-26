import mysql.connector

def open_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yusif2003!",
        database="onlinetrade"
    )
    return conn

def close_connection(conn):
    conn.close()
