def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# args empacota os dados dentro de uma tupla(str)
# sendo que *variavel desempacota


numero = 1, 2, 3, 4, 5, 6, 7, 78, 10
soma = sum(*numero)
print(soma)

print(sum(numero))
