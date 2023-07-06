num = input("Digite um número inteiro: ")


if(num.isdigit()):
    num = int(num)

    if num % 2 == 0 :
        print("par")
    else:
        print("impar")
else:
    print("ERROR")
