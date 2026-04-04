import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from --Yang Ou-- in 3308.'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://yang_ou_postgres_user:Lmfaixi91SgYxM5XesWl5lEz91RJ2mNx@dpg-d78okfia214c73acrhgg-a/yang_ou_postgres")
    conn.close()
    return 'Database Connection Successful.'

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://yang_ou_postgres_user:Lmfaixi91SgYxM5XesWl5lEz91RJ2mNx@dpg-d78okfia214c73acrhgg-a/yang_ou_postgres")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
