from flask import Flask, redirect, url_for
from flask import render_template, request
from flask_mysqldb import MySQL
app = Flask('__name__')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'burjo_shop'

mysql = MySQL (app)

@app.route('/',methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        details = request.form
        username = details['username']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('profil'))

    return render_template("login.html")

@app.route('/daftar/',methods=['GET', 'POST'])
def daftar():

    if request.method == "POST":
        details = request.form
        username = details['username']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))

    return render_template("daftar.html")


@app.route('/profil/')
def profil():

    return render_template('profil.html', title='Profil')

@app.route('/menu/')
def menu():

    return render_template("menu.html")

@app.route('/contact/')
def contact():

    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)