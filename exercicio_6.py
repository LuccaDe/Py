# Exercício 6
# Saúda o usuário de acordo com a hora do dia

input_hora = input('Digite a hora: ')

try:
    hora = int(input_hora)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora <= 17:
        print('Boa tarde!')
    elif hora <= 23:
        print("Boa noite!")
    else:
        print('Esta não é uma hora válida.')
except:
    print('Este não é um formato válido.')