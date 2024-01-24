caminho = 'mod2/writefiles/write.txt'

with open(caminho, 'w+', encoding="utf-8") as arquivo: 
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(('linha 3\n', 'linha 4\n'))
    
    arquivo.seek(0, 0) # exibe por posição
    print(arquivo.read())
    

with open(caminho, 'r', encoding="utf") as arquivo:
    print(arquivo.read())