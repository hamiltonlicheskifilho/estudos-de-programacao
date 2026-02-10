# ==================================================
# Exercício: Procurando uma string dentro de outra
# Objetivo: Ler o nome de uma pessoa e informar se
# existe "SILVA" no nome.
# ==================================================

# Entrada de dados
nome = str(input('Digite seu nome: ')).strip()

# Processamento
tem_silva = 'SILVA' in nome.upper()

# Saída de dados
print(tem_silva)