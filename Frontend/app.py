from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
#from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'FLASK_CHECK'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


def get_connection():
    try:
        db_con = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='FLASK_CHECK')
    except mysql.connector.Error as err:
        app.logger.debug("Error")
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        app.logger.info("Created successfully")
        return db_con

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

# class LoginForm(Form):
#     email = StringField('Email', [validators.Length(min=17, max=17)])
#     token = PasswordField('Password', [validators.DataRequired()])


@app.route('/login', methods=['GET','POST'])
def login():
    #form = LoginForm(request.form)
    if request.method == 'POST':
        email = request.form['email']
        tokendb = request.form['token']
        db_con = get_connection()
        cur = db_con.cursor()

        result = cur.execute("SELECT * FROM ADMIN WHERE EMAIL = %s", (email,))
        app.logger.info("Email:{}".format(email))

        data = cur.fetchone()

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
