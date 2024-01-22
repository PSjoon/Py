pessoa = {
    'nome': 'Joao', 
    'sobrenome': 'Santos',
    'list': [0, 1, 2]
}

pessoa2 = pessoa.copy(pessoa)

pessoa2['nome'] = 'Pedro'
pessoa2['list'][1] = 5

print(pessoa)
print(pessoa2)
