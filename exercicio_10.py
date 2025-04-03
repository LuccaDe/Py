# Exercício 10
# Analisa qual é a letra que mais apareceu na frase
# Sugestão: Solicitar a frase para o usuário

frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum'

i = 0
contador = 0
maior_qtd = 0
maior_letra = ''

while i < len(frase):
    letra = frase[i].lower()

    i += 1

    if letra == ' ':
        continue

    contador = frase.count(letra)

    if contador > maior_qtd:
        maior_qtd = contador
        maior_letra = letra

print(f'A letra que apareceu mais vezes foi "{maior_letra}", aparecendo {maior_qtd} vezes.')
