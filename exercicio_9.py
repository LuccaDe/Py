while True:
    resultado = 0

    try:
        input_number_1 = input('Digite o primeiro número: ')
        number_1 = float(input_number_1)

        input_number_2 = input('Digite o segundo número: ')
        number_2 = float(input_number_2)

        print()
        print(25 * '-')
        print()

        try:
            print('[A]dição - [S]ubtração - [M]ultiplicação - [D]ivisão ')
            print()

            print(25 * '-')
            print()
            operador = input('Escolha a operação: ')
            print()

            operador = operador.lower()

            if operador == 'a':
                resultado = number_1 + number_2
            elif operador == 's':
                resultado = number_1 - number_2
            elif operador == 'm':
                resultado = number_1 * number_2
            elif operador == 'd':
                resultado = number_1 / number_2
            else:
                print('Operador inválido')
                resultado = None
        except:
            print()
            print('Operador inválido.')

        if resultado is not None: 
            print(f'O resultado é {resultado:.2f}')
    except:
        print()
        print('Número inválido.')

    print()
    escolha = input('Você deseja realizar mais uma operação? [S/N] ').lower()

    if escolha[0] == 'n':
        break

    print()
    print(30 * '-')
    print()

