# lista = [31, 1, 45, 41, 89]
# lista.sort() # ordenar lista
# print(lista)

# lista = [
#     {'nome': 'Joao', 'sobrenome': 'Santos'},
#     {'nome': 'Pedro', 'sobrenome': 'Silva'},
#     {'nome': 'Ana', 'sobrenome': 'Ferreira'},
#     {'nome': 'Maria', 'sobrenome': 'Anabeth'},
    
# ]

# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()
    

# lista1 = sorted(lista, key=lambda item:item['nome'])
# lista2 = sorted(lista, key=lambda item:item['sobrenome'])

# exibir(lista1)
# exibir(lista2 )

def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return x + y

# def  criarMultiplicador(multiplicador):
#     def  multiplica(numero):
#         return numero * multiplicador(numero)
#     return multiplica

print(
    executa(
        lambda x, y : x + y,
        2, 3
    )
)

# duplica = criarMultiplicador(2)
duplica = executa(
    lambda multiplicador: lambda numero: numero * multiplicador, 2
) 

print(duplica(2))