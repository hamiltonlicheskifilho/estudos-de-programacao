# ==================================================
# Módulo: Listas e Sorteios
# Descrição: Exercícios de fundamentos em Python
# envolvendo operações matemáticas, módulos e listas
# ==================================================

# Imports
from random import choice, shuffle
from time import sleep

# ==================================================
# Exercício: Sorteando um item na lista
# Objetivo: Sortear um dos quatro alunos para 
# apagar o quadro, lendo os nomes dos alunos 
# e mostrando o escolhido.
# ==================================================

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


# ==================================================
# Exercício: Sorteando uma ordem na lista
# Objetivo: Sortear a ordem de apresentação de 
# trabalhos escolares, lendo os nomes dos quatro alunos
# e mostrando a lista final.
# ==================================================

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
