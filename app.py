from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config['MYSQL_Host'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'desafio3'

mysql = MySQL(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

#@app.route("/contato")
#def contato():
#    return render_template('contato.html')

@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/contato', methods=['GET','POST'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)', (email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return 'Sucesso!' and render_template('contato.html')
    return render_template('contato.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)