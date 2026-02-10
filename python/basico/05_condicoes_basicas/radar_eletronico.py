# ==================================================
# Exercício: Radar eletrônico
# Objetivo: Ler a velocidade do carro. Se ele 
# ultrapassar 80Km/h, mostrar uma mensagem dizendo 
# que ele foi multado. A multa custa R$7,00 
# por cada Km acima do limite.
# ==================================================

# Imports
from time import sleep

# Funções auxiliares
def linha():
    print('-=-' * 20)

# Entrada de dados
linha()
velocidade = int(input('Qual a velocidade atual do carro? '))
linha()

print('ANALISANDO...')
linha()
sleep(2)

# Processamento
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7

# Saída de dados
if velocidade > 80:
    print(f'Você foi multado! A multa é de R$ {multa:.2f}')
else:
    print('Velocidade dentro do limite. Tenha uma boa viagem!')