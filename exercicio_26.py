# Exercício 26
# Listar tarefas com as opções de DESFAZER e REFAZER

import os

todo = []
removidos = []


def listar():
    print('TAREFAS: ', *todo, sep='\n', end='\n\n')


while True:
    print('Comandos: Listar, Desfazer e Refazer')
    acao = input('Digite uma tarefa ou comando: ').strip().lower()

    if acao == 'listar':
        print()
        listar()
    elif acao == 'desfazer':
        if not todo:
            print()
            print('NADA A DESFAZER', end='\n\n')
        else:
            removidos.append(todo.pop())
            print()
        
        listar()
    elif acao == 'refazer':
        if not removidos:
            print()
            print('NADA A REFAZER', end='\n\n')
        else:
            todo.append(removidos.pop())
            print()
        
        listar()
    elif acao == 'clear':
        os.system('clear')
    elif acao == 'exit':
        break
    else:
        todo.append(acao)
        print()
        listar()
