class Pessoa:
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def falar_nome(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...
    
class Aluno(Pessoa):
    ...
    
cliente = Cliente('Pedro', 'Santos')
cliente.falar_nome()

aluno = Aluno('Pedro', 'Santos')
aluno.falar_nome()

help(Cliente)
