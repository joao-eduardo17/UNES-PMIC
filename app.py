from flask import Flask, render_template
from flask_mysqldb import MySQL

app.config['MYSQL_Host'] = 127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contatos'

app = Flask("__name__")

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')
@app.route("/contato")
def contato():
    return render_template('contato.html')
@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html')
@app.route('/contatos', methods=['GET','POST'])
def contatos:
    if request.method == 'POST':
		email = request.form['email']
		assunto = request.form['assunto']
		descricao = request.form['descrição']

		cur = mysql.connection.cursor()
		cur.execute('INSERT INTO contatos(email, assunto, descricao) VALUES (%s %s %s)', (email, assunto, descricao))

		mysql.connection.commit()

		cur.close()

		return 'Sucesso!'

	return render_template('contatos.html')