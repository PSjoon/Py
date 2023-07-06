hora = input("Digite um horário: ")

if (hora.isdigit()):
    hora = int(hora)

    if(hora < 0 or hora > 23):
        print("ERROR")
    else:
        if(hora >= 6 and hora <= 12):
            print("Bom dia")
        elif(hora >= 13 and hora <= 18):
            print("Boa tarde")
        elif(hora >= 19 and hora <= 23):
            print("Boa noite")
        else:
            print("Boa madrugada")
else:
    print("não número inteiro")
