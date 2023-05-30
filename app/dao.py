from models import Filme, Usuario

SQL_DELETA_FILME = 'delete from filme where id = %s'
SQL_FILME_POR_ID = 'SELECT id, nome, categoria, ano from filme where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_FILME = 'UPDATE filme SET nome=%s, categoria=%s, ano=%s where id = %s'
SQL_BUSCA_FILMES = 'SELECT id, nome, categoria, ano from filme'
SQL_CRIA_FILME = 'INSERT into filme (nome, categoria, ano) values (%s, %s, %s)'


class FilmeDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, filme):
        cursor = self.__db.connection.cursor()

        if (filme.id):
            cursor.execute(SQL_ATUALIZA_FILME, (filme.nome, filme.categoria, filme.ano, filme.id))
        else:
            cursor.execute(SQL_CRIA_FILME, (filme.nome, filme.categoria, filme.ano))
            filme.id = cursor.lastrowid
        self.__db.connection.commit()
        return filme

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_FILMES)
        filmes = traduz_filmes(cursor.fetchall())
        return filmes

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_FILME_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Filme(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_FILME, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_filmes(filmes):
    def cria_filme_com_tupla(tupla):
        return Filme(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_filme_com_tupla, filmes))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
