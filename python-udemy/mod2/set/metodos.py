# conjunto = set()

# conjunto.add('Pedro')
# conjunto.update(('olá', 1, 2, 3))
# conjunto.discard('olá')  
# print(conjunto)

conjunto = {1, 2, 3}
conjunto2 = {4, 5, 6, 3}
print(conjunto | conjunto2) # união de conjuntos
print(conjunto & conjunto2) # intersecção de conjuntos
print(conjunto - conjunto2) # diferença a esquerda
print(conjunto ^ conjunto2) # diferença simétrica
