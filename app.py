from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Cole Akers in 3308'


@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://akers_flask_lab10_db_user:q2hbLB5oMeWlBSmKZkQGYv1AfeGLg0QH@dpg-cvm2ffggjchc73evir7g-a.oregon-postgres.render.com/akers_flask_lab10_db")
    conn.close()
    return "Successfully connected to the database!"



@app.route('/db_create')
def tessting():
    conn = psycopg2.connect("postgresql://akers_flask_lab10_db_user:q2hbLB5oMeWlBSmKZkQGYv1AfeGLg0QH@dpg-cvm2ffggjchc73evir7g-a/akers_flask_lab10_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
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