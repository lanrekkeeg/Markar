from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
#from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import mysql.connector
from mysql.connector import errorcode
from config import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'FLASK_CHECK'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/aboutdash')
def aboutdash():
    return render_template('about-dash.html')

@app.route('/dashboardt')
def dasht():
    return render_template('dashboard-t.html')

@app.route('/dashboards')
def dashs():
    return render_template('dashboard-s.html')

@app.route('/login', methods=['GET','POST'])
def login():
    #form = LoginForm(request.form)
    if request.method == 'POST':
        email = request.form['email']
        tokendb = request.form['token']
        data = {}

        if data is not None:
            token = data[1]

            if token == tokendb:
                app.logger.info('TOKEN MATCHED')
                return render_template('dashboard-t.html')

            else:
                app.logger.info('INCORRECT TOKEN')
        else:
            app.logger.info('NO RECORD FOUND')

    return render_template('login.html')
    #return redirect(url_for('home'))


if __name__ == '__main__':
    #app.secret_key = 'secret123'
    app.run(debug=True)
