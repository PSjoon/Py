def soma(*args):
    total = 0
    for numeroSoma in args:
        total += numeroSoma
    return total

# args empacota os dados dentro de uma tupla(str), podendo ser facilmente alterada para lista utilizando list(args)
# sendo que *variavel desempacota


numero = 1, 2, 3, 4, 5, 6, 7, 8, 10
soma2 = soma(*numero)
print(soma2)
print(numero)

# print(sum(numero))
