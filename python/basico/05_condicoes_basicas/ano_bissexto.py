# ==================================================
# Exercício: Ano Bissexto
# Objetivo: Ler um ano qualquer e mostrar se ele é bissexto.
# ==================================================

# Imports
from time import sleep
from datetime import date

# Funções auxiliares
def linha():
    print('-=-' * 20)

# Entrada de dados
linha()
ano = int(input('Digite o ano para ser analisado, ou 0 para o ano atual: '))
linha()

print('Analisando...')
linha()
sleep(2)

# Processamento
if ano == 0:
    ano = date.today().year

# Saída de dados
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} NÃO é BISSEXTO.')