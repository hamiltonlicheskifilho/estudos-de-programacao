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