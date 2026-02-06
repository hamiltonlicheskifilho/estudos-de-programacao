# ==================================================
# Exercício: Média Aritmética
# Objetivo: Ler duas notas e calcular a média
# ==================================================

# Entrada de dados
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Processamento
media = (nota1 + nota2) / 2

# Saída de dados
print(f'A média das notas é {media:.2f}')


# ==================================================
# Exercício: Conversor de Medidas
# Objetivo: Converter metros para cm e mm
# ==================================================

# Entrada de dados
medida = float(input('Digite uma distância em metros: '))

# Processamento
cm = medida * 100
mm = medida * 1000

# Saída de dados
print(f'{medida} m corresponde a {cm:.0f} cm e {mm:.0f} mm')


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


# ==================================================
# Exercício: Pintando Parede
# Objetivo: ler a largura e a altura de uma parede
# em metros e calcular a quantidade de tinta necessária
# para pintá-la
# ==================================================

# Entrada de dados
largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))

# Processamento
area = largura * altura
tinta = area / 2  # 1 litro de tinta para cada 2 m²

# Saída de dados
print(f'Sua parede tem dimensões de {largura} m x {altura} m e área de {area:.2f} m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f} L de tinta.')


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


# ==================================================
# Exercício: Reajuste Salarial
# Objetivo: ler o salário de um funcionário
# e mostrar o novo valor com 15% de aumento
# ==================================================

# Entrada de dados
salario_funcionario = float(input('Digite o salário do funcionário: R$ '))

# Processamento
# Duas formas de calcular o aumento (optei pela porcentagem explícita)
aumento_salario = salario_funcionario + (salario_funcionario * 15 / 100)

# Saída de dados
print(
    f'O salário do funcionário era R$ {salario_funcionario:.2f} '
    f'e, após um aumento de 15%, passou a ser R$ {aumento_salario:.2f}.'
)


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
