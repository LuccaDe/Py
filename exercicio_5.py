input_numero = input('Digite um número inteiro: ')

try:
    numero = int(input_numero)

    if numero % 2 == 0:
        print('Este número é par.')
    else:
        print('Este número é ímpar.')
except:
    print('Este não é um número inteiro.')
