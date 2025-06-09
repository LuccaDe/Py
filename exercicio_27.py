# Exercício 27
# Adicionar a funcionalidade de exportar a lista (presenteno exercício anterior) em JSON
# OBS.: Houve uma alteração no código para melhorar sua eficiência

import os
import json


def listar():
    print()
    print('TAREFAS: ', *todo, sep='\n', end='\n\n')
    return

def desfazer(lista_todo, lista_removidos):
    if not lista_todo:
        print()
        print('NADA A DESFAZER', end='\n\n')
        return
    
    lista_removidos.append(lista_todo.pop())
    print()
    listar()

def adicionar(lista_todo, item):
    lista_todo.append(item)
    print()

    listar()

def refazer(lista_todo, lista_removidos):
    if not lista_removidos:
        print()
        print('NADA A REFAZER', end='\n\n')
        return
    
    lista_todo.append(lista_removidos.pop())
    print()
    listar()

def limpar():
    os.system('clear')
    return

def ler(lista_todo, caminho):
    dados = []

    try:
        with open(caminho, 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('CRIANDO ARQUIVO...', end='\n\n')
        salvar(lista_todo, caminho)
    
    return dados

def salvar(lista_todo, caminho):
    dados = lista_todo

    with open(caminho, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo,indent=2)


CAMINHO_ARQUIVO = 'todo.json'
todo = ler([], CAMINHO_ARQUIVO)
removidos = []

while True:
   print('Comandos: Listar, Desfazer e Refazer')

   acao = input('Digite uma tarefa ou comando: ').strip().lower()

   if acao == 'fechar':
    break

   metodos = {
    'listar': lambda: listar(),
    'desfazer': lambda: desfazer(todo, removidos),
    'adicionar': lambda: adicionar(todo, acao),
    'refazer': lambda: refazer(todo, removidos),
    'limpar': lambda: limpar(),
   }

   exec = metodos.get(acao) if acao in metodos.keys() else metodos['adicionar']

   exec()
   salvar(todo, CAMINHO_ARQUIVO)
