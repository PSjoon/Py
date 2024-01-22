pessoa = {
    'nome': 'Joao', 
    'sobrenome': 'Santos',
    'idade' : 18
}

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

pessoa.setdefault('idade', 0)

print(pessoa)

# print(pessoa.pop('nome'))
print(pessoa.popitem())
print(pessoa)
print(pessoa.update({
    'nome': 'Pedro', 
    'sobrenome': 'Silva',
    'idade': 20
}))

print(pessoa)
