from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
#from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import mysql.connector
from mysql.connector import errorcode
from config import *
import requests
import json
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'FLASK_CHECK'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
data_ = [{
  "Name": "Faisal",
  "Email": "p156058@nu.edu.pk",
  "Task No": "1",
  "Marks": "10"
},
 {
  "Name": "Faisal",
  "Email": "p156058@nu.edu.pk",
  "Task No": "1",
  "Marks": "20"
}, {
  "Name": "Faisal",
  "Email": "p156058@nu.edu.pk",
  "Task No": "1",
  "Marks": "10"
}]
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "Name", # which is the field's name of data key 
    "title": "Name", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "Email",
    "title": "Email",
    "sortable": True,
  },
  {
    "field": "Task No",
    "title": "Task No",
    "sortable": True,
  },
  {
    "field": "Marks",
    "title": "Marks",
    "sortable": True,
  }
]
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
        headers = {'authorization':tokendb, 'Content-type':'application/json'}
        data= {"admin_email": email}
        out = requests.post(markar_api+"/ValidateAdmin", data=json.dumps(data), headers=headers)

        print(out.json())
        data = out.json()
        if data['authorize']:
            app.logger.info('TOKEN MATCHED')
            return render_template("tables.html",data=data_,columns=columns, title='Markar Grades')
            #return render_template('dashboard-t.html')
        else:
            app.logger.info('INCORRECT TOKEN')
       
    return render_template('login.html')
    #return redirect(url_for('home'))


if __name__ == '__main__':
    #app.secret_key = 'secret123'
    app.run(debug=True)