# Exercício 22
# Ordenar os produtos por preço em ordem crescente, gerando uma nova lista por deep copy

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda d: d['preco'])

for i in produtos_ordenados_por_preco:
    print(f'{i['nome']}: R${i['preco']:.2f}')