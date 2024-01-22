def criarSaudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


saudacao = criarSaudacao('bom dia')

print(saudacao('Luiz'))
