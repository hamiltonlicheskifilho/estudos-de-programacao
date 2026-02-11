# ==================================================
# Exercício: Primeira e última ocorrência de uma string
# Objetivo: Ler uma frase e mostrar quantas vezes aparece
# a letra "A" e em que posição ela aparece a primeira
# e a última vez.
# ==================================================

# Entrada de dados
frase = str(input('Digite uma frase: ')).strip().upper()

# Processamento
quantidade_a = frase.count('A')
primeira_posicao = frase.find('A') + 1
ultima_posicao = frase.rfind('A') + 1

# Saída de dados
print(f'A letra A aparece {quantidade_a} vezes.')
print(f'Primeira posição: {primeira_posicao}')
print(f'Última posição: {ultima_posicao}')