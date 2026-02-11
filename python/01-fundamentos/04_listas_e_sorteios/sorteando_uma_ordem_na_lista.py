# ==================================================
# Exercício: Sorteando uma ordem na lista
# Objetivo: Sortear a ordem de apresentação de 
# trabalhos escolares, lendo os nomes dos quatro alunos
# e mostrando a lista final.
# ==================================================

# Imports
from random import shuffle
from time import sleep

# Entrada de dados
primeiro_aluno_ordem = input('Primeiro aluno: ')
segundo_aluno_ordem = input('Segundo aluno: ')
terceiro_aluno_ordem = input('Terceiro aluno: ')
quarto_aluno_ordem = input('Quarto aluno: ')

# Processamento
lista_ordem = [primeiro_aluno_ordem, segundo_aluno_ordem, terceiro_aluno_ordem, quarto_aluno_ordem]
shuffle(lista_ordem)

# Saída de dados
print('A ordem de apresentação será:')
sleep(2)
print(lista_ordem)