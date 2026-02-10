# ==================================================
# Exercício: Conversor de Moedas
# Objetivo: Ler um valor em reais e convertê-lo
# para outras moedas (valores fixos para exercício)
# ==================================================

# Entrada de dados
valor = float(input('Digite o valor desejado: R$ '))

# Processamento
dolar = valor / 5.29
libra_egipcia = valor / 0.11

# Saída de dados
print(f'Com o valor de R${valor:.2f} você consegue fazer o câmbio para:')
print(f'Dólar: {dolar:.2f}')
print(f'Libra Egípcia: {libra_egipcia:.2f}')