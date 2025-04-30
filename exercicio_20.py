# Exercício 20
# Aumentar os preços dos produtos a seguir em 10%, gerando uma nova lista por deep copy

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)

for i in novos_produtos:
    i['preco'] = round(i['preco'] * 1.1, 2)
    print(f'{i['nome']}: R${i['preco']}')