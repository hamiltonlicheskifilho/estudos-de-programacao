# ==================================================
# Exercício: Sorteando um item na lista
# Objetivo: Sortear um dos quatro alunos para 
# apagar o quadro, lendo os nomes dos alunos 
# e mostrando o escolhido.
# ==================================================

# Imports
from random import choice
from time import sleep

# Entrada de dados
primeiro_aluno = input('Primeiro aluno: ')
segundo_aluno = input('Segundo aluno: ')
terceiro_aluno = input('Terceiro aluno: ')
quarto_aluno = input('Quarto aluno: ')

# Processamento
lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
sorteado = choice(lista_alunos)

# Saída de dados
print('A pessoa sorteada foi:')
sleep(2)
print(f'{sorteado}')