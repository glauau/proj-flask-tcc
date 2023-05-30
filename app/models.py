class Filme:
    def __init__(self, nome, categoria, ano, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.ano = ano

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
