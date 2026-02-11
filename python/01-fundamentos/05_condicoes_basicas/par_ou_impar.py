# ==================================================
# Exercício: Par ou Ímpar
# Objetivo: Ler um número inteiro e mostrar na tela 
# se ele é PAR ou ÍMPAR.
# ==================================================

# Imports
from time import sleep

# Funções auxiliares
def linha():
    print('-=-' * 20)

# Entrada de dados
linha()
numero = int(input('Me diga um número qualquer: '))
linha()

print('Analisando...')
linha()
sleep(2)

# Processamento e Saída de dados
if numero % 2 == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é ÍMPAR')
