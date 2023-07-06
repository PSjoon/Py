nome = input("Digite seu nome: ")

if(nome.isdigit):
    cont = nome.__len__()
    if(cont <= 4):
        print("Nome muito curto")
    elif(cont >= 5 and cont <= 6):
        print("Nome normal")
    else:
        print("Nome muito grande")
else: 
    print("ERROR")
