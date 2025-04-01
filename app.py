from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Cole Akers in 3308'


@app.route('/db_test')
def tessting():
    conn = psycopg2.connect("postgresql://akers_flask_lab10_db_user:q2hbLB5oMeWlBSmKZkQGYv1AfeGLg0QH@dpg-cvm2ffggjchc73evir7g-a/akers_flask_lab10_db")
    conn.close()
    return "Database connection Successful"