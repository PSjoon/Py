class Pessoa: 
    ano_atual = 2024
    
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade
        
    def anoNascimento(self):
        return Pessoa.ano_atual - self.idade
    
pessoa1 = Pessoa('Pedro', 33)
pessoa2 = Pessoa('Helena', 11)

print(pessoa1.__dict__)
print(vars(pessoa1))