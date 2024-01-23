produto = {
    'name': 'Caneta',
    'preco': 25,
    'categoria' : 'escritório'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}

print(dc)

s1 = {i for i in range(10)}
print(s1)