# ==================================================
# Exercício: Seno, Cosseno e Tangente
# Objetivo: Ler um ângulo e mostrar o valor do seno,
# cosseno e tangente.
# ==================================================

# Imports
from math import sin, cos, tan, radians

# Entrada de dados
angulo = float(input('Digite o ângulo desejado em graus: '))

# Processamento
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

# Saída de dados
print(f'O ângulo de {angulo}° tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo}° tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo}° tem a TANGENTE de {tangente:.2f}')