import pprint

# print(list(range(10)))
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# lista = []

# for numero in range(10):
#     lista.append(numero)  
# # print(lista)


# lista = [numero * 2 for numero in range(10)]

# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco': 30},
]

novosProdutos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] >= 10
]
p(novosProdutos)

# # lista = [numero for numero in range(10) if numero <= 5]
# p(lista)





