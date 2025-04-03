# Exercício 16
# Retorna para o usuário se o número é par ou ímpar, utilizando Closure

def par_impar(n):
    if n % 2 == 0:
        return 'PAR'
    return 'ÍMPAR'
    

input_numero = input('Digite um número: ')

resultado = par_impar(int(input_numero))

print(f'O número {input_numero} é {resultado}')