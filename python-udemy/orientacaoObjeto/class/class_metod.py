class Pessoa: 
    ano_atual = 2024
    
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade
    
    @classmethod
    def metodo_classe(cls):
        print('hey')
        
    @classmethod
    def criar_com_50(cls, name):
        return cls(name, 50)
    
pessoa1 = Pessoa('Pedro', 33)
pessoa2 = Pessoa.criar_com_50('Helena')
print(pessoa2.name, pessoa2.idade )

# Pessoa.metodo_classe()
print(Pessoa.ano_atual)
pessoa1.metodo_classe()