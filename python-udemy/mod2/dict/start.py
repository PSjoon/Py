# pessoa = dict(nome = 'Pedro', sobrenome = 'Santos')

# pessoa = {
#     'nome': 'Pedro',
#     'sobrenome': 'Santos'
# }

# pessoa['idade'] = 18

# print(pessoa, type(pessoa))

pessoa = {}
chave = 'nome'

pessoa[chave] = 'Luiz'
pessoa['sobrenome'] = 'Santos'

print(pessoa[chave])
pessoa[chave] = 'Maria'

del pessoa['sobrenome']

print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome') is None:
    print('nao existe')
    