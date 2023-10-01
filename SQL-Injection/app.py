from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
# MYSQL CONFIG FILE
app.secret_key = os.getenv('SECRET_KEY')
  
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
mysql = MySQL(app)


@app.route('/')
def hello():
  return render_template("testlogin.html") 

@app.route('/login', methods =['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = % s AND password  = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            # session['userid'] = user['userid']
            session['name'] = user['email']
            # session['email'] = user['email']
            message = session['name']
            if 'admin@lab.com' in session['name']:
                return render_template('admin.html', message = message)
            else:
                return render_template('fail.html', message= message)
        else:
            message = 'Please enter correct email / password !'
    return render_template('testlogin.html', message = message)

@app.route('/register', methods =['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST' and 'password' in request.form and 'email' in request.form :
        # username = request.form['name']
        password = request.form['password']
        username = request.form['email']
        print(username,password)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        modes='ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'
        cursor.execute("SET session sql_mode=% s",[modes])
        cursor.execute('SELECT * FROM users WHERE email = % s', (username, ))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', username):
            message = 'Invalid email address !'
        elif not password or not username:
            message = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO users VALUES (% s, % s)', (username, password, ))
            mysql.connection.commit()
            message = 'You have successfully registered !'
    elif request.method == 'POST':
        message = 'Please fill out the form !'
    return render_template('testlogin.html', message = message)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('name',None)
    return redirect(url_for('login'))

if __name__ == "__main__":
  app.run()