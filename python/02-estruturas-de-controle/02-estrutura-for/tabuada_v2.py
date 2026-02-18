
# ==================================================
# Exercício: Tabuada v.2
# Objetivo: Ler e mostrar a tabuada que o usuário escolher.
# ==================================================

# Imports
from time import sleep

# Funções auxiliares
def linha():
	print('-=' * 30)

# Entrada de dados
linha()
print('\033[1m\033[4mTABUADA V.2.0\033[m')
linha()
sleep(1)

num = int(input('Digite um número para ver sua tabuada: '))

# Processamento e Saída de dados
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
