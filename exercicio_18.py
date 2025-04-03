# Exercício 18
# Quiz
# Sugestão: Adicionar perguntas dinâmicamente para personalizar o Quiz

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

contador_acertos = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}\n")
    print('Opções:')

    for index, opcao in enumerate(pergunta['Opções']):
        print(f"{chr(ord('a') + index)}) {opcao}")

    try:
        resposta = ord(input('Escolha uma opção: ').lower()) - 97

        if pergunta['Opções'][resposta] == pergunta['Resposta']:
            print('Acertou :-)')
            contador_acertos += 1
        else:
            print('Errou :-(')
    except (ValueError, IndexError):
        print('Errou! Esta não é uma opção válida.')
        print()
        continue

    print()

print(f'Você acertou {contador_acertos} de {len(perguntas)} perguntas.')