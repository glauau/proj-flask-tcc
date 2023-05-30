from flask import Flask, render_template, request, redirect, session, flash, url_for
from models import Filme, Usuario
from dao import FilmeDao, UsuarioDao
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'alura'
app.config['MYSQL_HOST'] = "mysqlsrv"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "filmoteca"
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)

filme_dao = FilmeDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    lista = filme_dao.listar()
    return render_template ('lista.html', titulo='Filmoteca', filmes=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect (url_for('login', proxima=url_for('novo')))
    else:
        return render_template('novo.html', titulo='Novo Filme')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    ano = request.form['ano']
    filme = Filme(nome, categoria, ano)
    filme_dao.salvar(filme)
    return redirect (url_for('index'))

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logado com sucesso.')
            proxima_pagina = request.form['proxima']
            return redirect (proxima_pagina)
    else:
        flash(' tente novamente, login não efetuado.')
        return redirect (url_for('login'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect (url_for('login', proxima=url_for('editar', id=id)))
    filme = filme_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Editando Filme', filme=filme)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    ano = request.form['ano']
    filme = Filme(nome, categoria, ano, id=request.form['id'])
    filme_dao.salvar(filme)
    return redirect (url_for('index'))

@app.route ('/deletar/<int:id>')
def deletar(id):
    filme_dao.deletar(id)
    flash('Filme removido.')
    return redirect (url_for('index'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado.')
    return redirect (url_for('index'))

app.run(host="0.0.0.0")
