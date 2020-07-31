from flask import Flask, render_template,redirect,session,url_for
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("login.html")

@app.route('/profile')
def login():
    return render_template("profile.html")


@app.route('/new')
def new_user():
    return render_template("register2.html")

if __name__ == '__main__':
    app.run(debug=True)

