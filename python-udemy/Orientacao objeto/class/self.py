class Pessoa: 
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome    

pessoa1 = Pessoa('Luiz', 'Silva')
pessoa2 = Pessoa('Pedro', 'Santos')

# pessoa1.nome = 'Pedro'
# pessoa1.sobrenome = 'Santos'

print(pessoa1.nome)
print(pessoa2.sobrenome)

class Carro:
    def __init__(self, name=''):
        self.name = name
    
    def acelerar(self):
        print(f'{self.name} está acelerando...')
        
        
fusca = Carro('fusca')
# print(fusca.name)
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(name='celta')
# print(celta.name)
celta.acelerar()
Carro.acelerar(celta)