# Exercício 25
# Criar uma função zipper de soma, ou seja, a função deve somar duas listas em ordem.
# Deve-se usar todos os valores da menor lista

def somar_listas(lista_a, lista_b):
    return [sum(i) for i in zip(lista_a, lista_b)]

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

print(somar_listas(l1, l2))