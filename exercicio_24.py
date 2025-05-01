# Exercício 24
# Criar uma função zipper, ou seja, a função deve unir duas listas em ordem.
# Deve-se usar todos os valores da menor lista

def unir_listas(a, b):
    tamanho = min(len(a), len(b))
    return [(a[i], b[i]) for i in range(tamanho)]

lista_a = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_b = ['BA', 'SP', 'MG', 'RJ']

print(unir_listas(lista_a, lista_b))