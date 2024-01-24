# uma função que podem retornar ela de volta, criando um loop
# util para dividfir problemas grandes em partes menores

# def recursivo(start=0, end=10):
    # caso recusivo:
    # contar até cchegar ao final
    
#     if start >= end:
#         return end
    
#     start += 1
#     return recursivo(start, end)


# print(recursivo()) 

def fatorial(numero):
    if numero <= 1:
        return 1 
    
    return numero * fatorial(numero -1)

print(fatorial(10))