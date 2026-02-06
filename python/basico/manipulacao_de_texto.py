# ==================================================
# Módulo: Manipulação de Texto
# Descrição: Exercícios de fundamentos em Python
# envolvendo strings e tratamento de texto.
# ==================================================

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
print(
    f'Seu nome em MAIÚSCULAS é: {maiusculas}',
    f'Seu nome em MINÚSCULAS é: {minusculas}',
    f'Seu nome tem ao todo {quantidade_letras_total} letras',
    f'Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras'
)


# ==================================================
# Exercício: Separando dígitos de um número
# Objetivo: Ler um número de 0 a 9999 e mostrar cada
# um dos dígitos separados.
# ==================================================

from time import sleep

# Entrada de dados
numero = int(input('Digite um número de 0 a 9999: '))

# Processamento
num = str(numero).zfill(4)

print(f'Analisando o número: {numero}...')
sleep(2)

# Saída de dados
print(
    f'Unidade: {num[3]}',
    f'Dezena: {num[2]}',
    f'Centena: {num[1]}',
    f'Milhar: {num[0]}'
)


# ==================================================
# Exercício: Verificando as primeiras letras de um texto
# Objetivo: Ler o nome de uma cidade e informar se ela
# começa ou não com a palavra "SANTO"
# ==================================================

# Entrada de dados
cidade = str(input('Digite o nome da cidade: ')).strip()

# Processamento
comeca_com_santo = cidade[:5].upper() == 'SANTO'

# Saída de dados
print(comeca_com_santo)


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
