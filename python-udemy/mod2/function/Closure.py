def criarSaudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


saudacao2 = criarSaudacao('bom dia')

print(saudacao2('Luiz'))
