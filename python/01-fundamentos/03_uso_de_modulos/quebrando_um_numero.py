# ==================================================
# Exercício: Quebrando um número
# Objetivo: Ler um número real e mostrar sua
# porção inteira.
# ==================================================

# Imports
from math import trunc

# Entrada de dados
numero_real = float(input('Digite um valor: '))

# Processamento
porcao_inteira = trunc(numero_real)

# Saída de dados
print(f'O valor digitado foi {numero_real} e sua porção inteira é {porcao_inteira}')