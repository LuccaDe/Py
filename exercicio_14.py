# Exercício 14
# Analisador de CPFs
# Sugestão: Transformar em um Gerador de CPFs

from sys import exit

cpf = input('Digite seu CPF: ').strip()
tamanho_cpf = len(cpf)

try:
    if tamanho_cpf == 11 or tamanho_cpf == 14:
        if not cpf.isdigit():
            cpf_separado = cpf.split('.')
            cpf_separado_fim = cpf_separado + cpf_separado[2].split('-')
            cpf_separado_fim.pop(2)

            cpf_formatado = ''.join(cpf_separado_fim)
        else:
            cpf_formatado = cpf

        if cpf_formatado == cpf_formatado[0] * tamanho_cpf:
            print(f'O CPF {cpf} NÃO é válido.')
            exit()

        multiplicadores = range(10, 1, -1)
        soma = 0
        j = 10
        resto = 0

        for i in multiplicadores:
            soma += i * int(cpf_formatado[j - i])

        soma *= 10
        resto = soma % 11

        primeiro_digito = resto if resto <= 9 else 0

        soma = 0
        j = 11
        multiplicadores = range(11, 1, -1)
        resto = 0

        for i in multiplicadores:
            soma += i * int(cpf_formatado[j -i])

        soma *= 10
        resto = soma % 11

        segundo_digito = resto if resto <= 9 else 0

        if primeiro_digito == int(cpf_formatado[-2]) and segundo_digito == int(cpf_formatado[-1]):
            print(f'O CPF {cpf} é VÁLIDO.')
        else:
            print(f'O CPF {cpf} NÃO é válido.')
    else:
        print('CPF inválido - Quantidade de dígitos não aceita.')
except IndexError as error_1:
    print('CPF Inválido - São permitidos apenas números e separadores.')