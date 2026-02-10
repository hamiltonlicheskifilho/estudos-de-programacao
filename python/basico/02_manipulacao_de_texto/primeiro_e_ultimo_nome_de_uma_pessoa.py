# ==================================================
# Exercício: Primeiro e último nome de uma pessoa
# Objetivo: Ler o nome completo de uma pessoa e mostrar
# o primeiro e o último nome separadamente.
# ==================================================

# Entrada de dados
nome = str(input('Digite seu nome completo: ')).strip()

# Processamento
nomes = nome.split()
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

# Saída de dados
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {ultimo_nome}')