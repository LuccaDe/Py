import os

palavra_secreta = input('Escolha uma palavra secreta: ')
os.system('cls')

palavra_secreta = palavra_secreta.lower()
palavra_formatada = ''
buffer = ''

tentativas = 0
escolha = None

while True:
    entrada = input('Digite uma letra: ').lower()

    if len(entrada) != 1:
        print('Digite apenas uma letra!')
        continue
    
    if entrada in palavra_secreta:
        buffer += entrada

    palavra_formatada = ''

    for j in palavra_secreta:
        if j in buffer:
            palavra_formatada += j
        else:
            palavra_formatada += '*'
    
    tentativas += 1

    if palavra_formatada == palavra_secreta:
        os.system('cls')
        print('Você ganhou! Parabéns!')
        print(f'A palavra era: {palavra_secreta.capitalize()}')
        print(f'Tentativas: {tentativas}')

        print()
        
        escolha = input('Deseja jogar novamente? [S/N]: ').lower()

        while escolha != 's' and escolha != 'n':
            os.system('cls')
            print('Esta não é uma opção válida.')
            escolha = input('Deseja jogar novamente? [S/N]: ').lower()

        if escolha.lower() == 's':
            print()
            
            palavra_secreta = input('Escolha outra palavra secreta: ').lower()
            palavra_formatada = len(palavra_secreta) * '*'
            buffer = ''

            tentativas = 0
            os.system('cls')
        else:
            os.system('cls')
            print('Obrigado por jogar! Até a próxima.')
            break
    else:
        print(f'Palavra formatada: {palavra_formatada}')


