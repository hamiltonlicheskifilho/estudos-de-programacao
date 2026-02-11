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