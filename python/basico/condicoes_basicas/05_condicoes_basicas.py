# ==================================================
# Módulo: Condições Simples
# Descrição: Exercícios de fundamentos em Python
# utilizando estruturas condicionais simples (if / else).
# ==================================================

# Imports
from random import randint
from time import sleep
from datetime import date

# Funções auxiliares
def linha():
    print('-=-' * 20)

# ==================================================
# Exercício: Jogo da Adivinhação v1.0
# Objetivo: Fazer o computador pensar em um número
# e o usuário tentar adivinhar.
# ==================================================

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


# ==================================================
# Exercício: Radar eletrônico
# Objetivo: Ler a velocidade do carro. Se ele 
# ultrapassar 80Km/h, mostrar uma mensagem dizendo 
# que ele foi multado. A multa custa R$7,00 
# por cada Km acima do limite.
# ==================================================

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


# ==================================================
# Exercício: Par ou Ímpar
# Objetivo: Ler um número inteiro e mostrar na tela 
# se ele é PAR ou ÍMPAR.
# ==================================================

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


# ==================================================
# Exercício: Custo da Viagem
# Objetivo: Ler a distância em km e calcular o valor 
# da passagem, cobrando R$0,50 por km para viagens 
# de até 200 km e R$0,45 para viagens mais longas.
# ==================================================

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


# ==================================================
# Exercício: Ano Bissexto
# Objetivo: Ler um ano qualquer e mostrar se ele é bissexto.
# ==================================================

# Entrada de dados
ano = int(input('Digite o ano para ser analisado, ou 0 para o ano atual: '))

# Processamento
if ano == 0:
    ano = date.today().year

# Saída de dados
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} NÃO é BISSEXTO.')
