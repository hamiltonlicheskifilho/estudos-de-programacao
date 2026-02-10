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