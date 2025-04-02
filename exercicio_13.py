from os import system
lista = ['teste 1', 'teste 2']
lista_enumerada = []

while True:
    escolha = input('Selecione uma opção\n'
                    '[I]nserir [A]pagar [L]istar: ').lower()
    
    counter = 0
    try:
        escolha = escolha.lower()
        tamanho_lista = len(lista)

        if escolha == 'i':
            valor = input('Valor: ')

            lista.append(valor)
            system('cls')
        elif escolha == 'a':
            index_str = input('Escolha o índice para apagar: ')
            
            if tamanho_lista != 0:
                if index_str.isdigit():
                    lista_enumerada = list(enumerate(lista))

                    index = int(index_str)
                    for j in lista_enumerada:
                        counter += 1
                        if index in j:
                            lista.pop(index)
                            system('cls')
                            
                            break
                        elif counter == tamanho_lista:
                            system('cls')
                            print('Não foi possível apagar este índice')
                else:
                    print('Não foi possível apagar este índice')
            else:
                print('Não foi possível apagar este índice')
        elif escolha == 'l':
            if tamanho_lista == 0:
                system('cls')
                print('Nada para listar')
            else:
                system('cls')
                for i, item in enumerate(lista):
                    print(i, item)
        else:
            system('cls')
            print('Opção inválida')
    except:
        system('cls')
        print('Opção inválida')
