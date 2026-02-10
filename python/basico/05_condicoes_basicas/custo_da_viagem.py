# ==================================================
# Exercício: Custo da Viagem
# Objetivo: Ler a distância em km e calcular o valor 
# da passagem, cobrando R$0,50 por km para viagens 
# de até 200 km e R$0,45 para viagens mais longas.
# ==================================================

# Imports
from time import sleep

# Funções auxiliares
def linha():
    print('-=-' * 20)

# Entrada de dados
linha()
distancia = float(input('Qual é a distância da sua viagem? '))
linha()

print('Analisando...')
linha()
sleep(2)

# Processamento
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45

# Saída de dados
print(f'Você está prestes a começar uma viagem de {distancia} km.')
print(f'O valor da sua passagem será de R$ {valor:.2f}')