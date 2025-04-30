# Exercício 21
# Ordenar os produtos por nome em ordem decrescente, gerando uma nova lista por deep copy

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda d: d['nome'], reverse=True)

for i in produtos_ordenados_por_nome:
    print(f'{i['nome']}: R${i['preco']:.2f}')