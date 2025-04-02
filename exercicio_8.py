nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
index = 0

while index < tamanho_nome:
    print(f'*{nome[index]}', end='')


    index += 1
