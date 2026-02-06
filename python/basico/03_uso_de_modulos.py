# ==================================================
# Módulo: Uso de Módulos
# Descrição: Exercícios de fundamentos em Python
# envolvendo o uso de módulos.
# ==================================================

# Imports
from math import trunc, hypot, sin, cos, tan, radians

# ==================================================
# Exercício: Quebrando um número
# Objetivo: Ler um número real e mostrar sua
# porção inteira.
# ==================================================

# Entrada de dados
numero_real = float(input('Digite um valor: '))

# Processamento
porcao_inteira = trunc(numero_real)

# Saída de dados
print(f'O valor digitado foi {numero_real} e sua porção inteira é {porcao_inteira}')


# ==================================================
# Exercício: Catetos e Hipotenusa
# Objetivo: Ler o comprimento de um cateto oposto 
# e do cateto adjacente de um triângulo retângulo e calcular
# o comprimento da hipotenusa.
# ==================================================

# Entrada de dados
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

# Processamento
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# Saída de dados
print(f'O valor da hipotenusa é {hipotenusa:.2f} unidades')


# ==================================================
# Exercício: Seno, Cosseno e Tangente
# Objetivo: Ler um ângulo e mostrar o valor do seno,
# cosseno e tangente.
# ==================================================

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

