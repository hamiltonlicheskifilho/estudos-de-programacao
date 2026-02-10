# ==================================================
# Exercício: Jogo da Adivinhação v1.0
# Objetivo: Fazer o computador pensar em um número
# e o usuário tentar adivinhar.
# ==================================================

# Imports
from time import sleep
from random import randint

# Funções auxiliares
def linha():
    print('-=-' * 20)

# Entrada de dados
linha()
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')
linha()

# Processamento
numero = int(input('Em que número eu pensei? '))
computador = randint(1, 5)
linha()

print('Pensando...')
sleep(2)
linha()

# Saída de dados
if numero == computador:
    print(f'Parabéns, você acertou! Eu pensei no número {computador}')
else:
    print(f'É... Eu pensei no número {computador}. Talvez na próxima!')
