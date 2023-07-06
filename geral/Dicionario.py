usuarios = {}
opcao = input("O que deseja realizar?\n" +
              "<I> - Para Inserir um usuário\n" +
              "<P> - Para Pesquisar um usuário\n" +
              "<E> - Para Excluir um usuário\n" +
              "<L> - Para Listar um usuário: \n").upper()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        chave = input("Digite o login: ").upper()
        nome = input("Digite o nome: ").upper()
        data = input("Digite a última data de acesso: ")
        estacao = input("Digite a última estação acessada: ").upper()
        usuarios[chave] = [nome, data, estacao]
    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n" +
                  "<P> - Para Pesquisar um usuário\n" +
                  "<E> - Para Excluir um usuário\n" +
                  "<L> - Para Listar um usuário: ").upper()


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])


def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto Eliminado")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)
