pessoa = {
    'nome': 'Joao', 
    'sobrenome': 'Santos',
}

# print(pessoa.values())

# for chave, valor in pessoa.items():
#     print(chave, valor)


# print({**pessoa, 'chave': 1})

def showArguments(*args, **kwargs): 
    print('não nomeados:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)
      
showArguments(1, 2, nome = 'Pedro')

