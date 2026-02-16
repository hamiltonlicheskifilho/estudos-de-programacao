# ==================================================
# Exercício: Pedra, Papel e Tesoura
# Objetivo: Fazer com que o programa joguqe Jokenpô 
# com você
# ==================================================

# Imports
from time import sleep
from random import randint

# Funções auxiliares
def linha():
	print('-=' * 30)

# Entrada de dados
linha()
print('\033[1mPEDRA PAPEL E TESOURA\033[m')
linha()
sleep(1)

print('''\033[1mPedra, Papel ou Tesoura?\033[m
	\033[1m[1]\033[m Pedra
	\033[1m[2]\033[m Papel
	\033[1m[3]\033[m Tesoura''')

# Processamento 
linha()
choice = int(input('Escolha, \033[1m1, 2\033[m ou \033[1m3\033[m: '))

computer = randint(1, 3)
moves = ['PEDRA', 'PAPEL', 'TESOURA']

linha()
print('\033[1mJO\033[m')
sleep(1)
print('\033[1mKEN\033[m')
sleep(1)
print('\033[1mPÔ\033[m')
sleep(1)

sleep(2)

# Saída de dados
linha()
if choice == computer:
    print(f'EMPATE! Você jogou {moves[choice - 1]} e o computador jogou {moves[computer - 1]}')
elif (choice == 1 and computer == 3) or \
     (choice == 2 and computer == 1) or \
     (choice == 3 and computer == 2):
    print(f'VITÓRIA! Você jogou {moves[choice - 1]} e o computador jogou {moves[computer - 1]}')
else:
    print(f'DERROTA! Você jogou {moves[choice - 1]} e o computador jogou {moves[computer - 1]}')
