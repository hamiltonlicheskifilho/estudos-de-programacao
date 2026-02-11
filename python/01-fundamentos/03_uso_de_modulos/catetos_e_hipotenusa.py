# ==================================================
# Exercício: Catetos e Hipotenusa
# Objetivo: Ler o comprimento de um cateto oposto 
# e do cateto adjacente de um triângulo retângulo e calcular
# o comprimento da hipotenusa.
# ==================================================

# Imports
from math import hypot

# Entrada de dados
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

# Processamento
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# Saída de dados
print(f'O valor da hipotenusa é {hipotenusa:.2f} unidades')