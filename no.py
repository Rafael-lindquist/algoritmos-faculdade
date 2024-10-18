from aluno import Aluno

class No():
    def __init__(self, valor: Aluno, proximo: "No") -> None:
        self.valor = valor
        self.proximo = proximo 

    def inserir(self, no: 'No'):
        self.proximo = no

    def remover():
        pass