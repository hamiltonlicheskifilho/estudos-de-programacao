
# ==================================================
# Exercício: Progressão Aritmética
# Objetivo: Ler o primeiro termo e a razão de uma PA.
# No final, mostrar os 10 primeiros termos dessa progressão.
# ==================================================

# Imports
from time import sleep

# Funções auxiliares
def linha():
	print('-=' * 30)

# Entrada de dados
linha()
print('\033[1m\033[4mPROGRESSÃO ARITMÉTICA\033[m')
linha()
sleep(1)

pa = int(input('Digite o PRIMEIRO TERMO: '))
rz = int(input('Digite a RAZÃO: '))

# Processamento e Saída de dados
decimo = pa + (10 - 1) * rz

for c in range(pa, decimo + rz, rz):
	print(c, end= ' → ')
print('FIM')
