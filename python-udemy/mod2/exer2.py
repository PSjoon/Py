# Exercício
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parametro

def mult(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = mult(2)
triplicar = mult(3)
quadruplicar = mult(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
