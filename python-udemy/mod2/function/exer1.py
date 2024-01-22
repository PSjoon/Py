def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multi = mult(1, 2, 3, 4, 5)
print(multi)


def par_impar(numero):
    return numero % 2 == 0


print(par_impar(2))
print(par_impar(3))
