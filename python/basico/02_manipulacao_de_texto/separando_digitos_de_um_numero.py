# ==================================================
# Exercício: Separando dígitos de um número
# Objetivo: Ler um número de 0 a 9999 e mostrar cada
# um dos dígitos separados.
# ==================================================

# Entrada de dados
numero = int(input('Digite um número de 0 a 9999: '))

# Processamento
num = str(numero).zfill(4)

print(f'Analisando o número: {numero}...')

# Saída de dados
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')