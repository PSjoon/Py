class Pessoa: 
    ano_atual = 2024
    
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade
        
    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
pessoa1 = Pessoa('Pedro', 33)
pessoa2 = Pessoa('Helena', 11)

print(Pessoa.ano_atual)
print(pessoa1.ano_nascimento())
print(pessoa2.ano_nascimento())