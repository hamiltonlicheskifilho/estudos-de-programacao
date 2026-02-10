# ==================================================
# Exercício: Calculando Descontos
# Objetivo: ler o valor de um produto e mostrar
# o novo preço com 5% de desconto
# ==================================================

# Entrada de dados
valor = float(input('Digite o valor do produto: R$ '))

# Processamento
valor_com_desconto = valor - (valor * 0.05)

# Saída de dados
print(
    f'O valor final do produto de R${valor:.2f}, '
    f'com 5% de desconto, será R${valor_com_desconto:.2f}.'
)