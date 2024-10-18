class Aluno:
    def __init__(self, nome: str, idade: int, notas: list) -> None:
        self.nome = nome
        self.idade = idade
        self.notas = notas
    
    def boasVindas(self):
        print(f"Olá {self.nome}")

    def media(self) -> float:
        return sum(self.notas) / len(self.notas)
    
    def exibirBoletim(self):
        print(f"Aluno: {self.nome}")
        print(f"Média: {self.media}")