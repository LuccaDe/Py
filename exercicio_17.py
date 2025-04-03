# Exercício 17
# Multiplicador com tratamento de erros e Closure
# Sugestão: Solicitar o multiplicador para o usuário escolher

from os import system

def operacoes(numero):
    def multiplica(fator):
        return numero * fator
    
    return multiplica


input_usuario = input('Digite o número a ser multiplicado: ')

try:
    int_input_usuario = int(input_usuario)
except Exception as error_1:
    print(f'{input_usuario} não é uma entrada válida.')
    exit()

resultado = operacoes(int_input_usuario)

input_multiplicador = input('Por quanto você deseja multiplicar? 2, 3, ou 4? ')

try:
    if len(input_multiplicador) != 1:
        print(f'{input_multiplicador} não é uma entrada válida.')
        exit()

    int_multiplicador = int(input_multiplicador)
    
    if int_multiplicador < 2 or int_multiplicador > 4:
        print(f'O número {int_multiplicador} não está entre as opções válidas.')
        exit()
except Exception as error_2:
    print(f'{input_multiplicador} não é uma entrada válida.')
    exit()
    

print(resultado(int_multiplicador))