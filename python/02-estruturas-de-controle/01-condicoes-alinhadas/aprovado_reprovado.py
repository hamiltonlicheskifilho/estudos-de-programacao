# ==================================================
# Exercício: Aprovando Empréstimo Bancário
# Objetivo: Calcular se a prestação mensal excede 30%
# do salário do comprador.
# ==================================================

# Imports
from time import sleep

# Funções auxiliares
def linha():
	print('-=' * 20)

# Entrada de dados
linha()
print('\033[1mAPROVANDO EMPRÉSTIMO BANCÁRIO\033[m')
linha()

valor_casa = float(input('Valor da casa (R$): '))
salario_comprador = float(input('Salário do comprador (R$): '))
anos_financiamento = int(input('Anos de financiamento: '))
linha()

# Processamento
prestacao_mensal = valor_casa / (anos_financiamento * 12)
limite_parcela = salario_comprador * (30 / 100)

print('ANALISANDO...')
linha()
sleep(2)

# Saída de dados
if prestacao_mensal <= limite_parcela:
	print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos_financiamento} '
          f'anos, sua prestação mensal será de R$ {prestacao_mensal:.2f}.')
	linha()
	print('Empréstimo pode ser CONCEDIDO!')
	print('Parabéns pela sua casa própria!')
else:
    print('Empréstimo NEGADO!')
    print('A prestação excede 30% da sua renda.')
