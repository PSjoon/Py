# def duplicar(numero):
#     return numero * 2

# print(duplicar(4))

def criarMultiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criarMultiplicador(2)
print(duplicar(2))