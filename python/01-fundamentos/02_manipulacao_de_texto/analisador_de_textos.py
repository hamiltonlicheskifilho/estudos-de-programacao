# ==================================================
# Exercício: Analisador de Textos
# Objetivo: Ler o nome completo de uma pessoa e mostrar:
# - O nome com todas as letras maiúsculas e minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome
# ==================================================

# Entrada de dados
nome = str(input('Digite seu nome completo: ')).strip()

# Processamento
maiusculas = nome.upper()
minusculas = nome.lower()
quantidade_letras_total = len(nome) - nome.count(' ')
primeiro_nome = nome.split()[0]

# Saída de dados
print(f'Seu nome em MAIÚSCULAS é: {maiusculas}')
print(f'Seu nome em MINÚSCULAS é: {minusculas}')
print(f'Seu nome tem ao todo {quantidade_letras_total} letras')
print(f'Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras')