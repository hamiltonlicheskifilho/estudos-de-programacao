# ==================================================
# Exercício: Aluguel de Carros
# Objetivo: Ler a quantidade de Km percorridos por
# um carro alugado e a quantidade de dias alugados.
# Calcular o valor a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.
# ==================================================

# Entrada de dados
km_percorridos = float(input('Digite quantos Km foram percorridos: '))
dias_alugados = int(input('Digite a quantidade de dias alugados: '))

# Processamento
valor_dia = 60
valor_km = 0.15
valor_pagar = (valor_dia * dias_alugados) + (valor_km * km_percorridos)

# Saída de dados
print(
    f'O valor total a pagar pelos dias alugados e Km rodados '
    f'é de R$ {valor_pagar:.2f}.'
)