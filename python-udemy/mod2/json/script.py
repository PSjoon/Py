import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada' : None,
}


# with open('mod2/json/saveOnJson.json', 'w', encoding='utf8') as arquivo: 
    # json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
    
with open('mod2/json/saveOnJson.json', 'r', encoding='utf8') as arquivo: 
    pessoa2 = json.load(arquivo)
    print(pessoa2)
