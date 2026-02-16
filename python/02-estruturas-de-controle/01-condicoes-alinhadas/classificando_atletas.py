# ==================================================
# Exercício: Classificando Altletas
# Objetivo: ler o ano de nascimento de um atleta e 
# mostrar sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
# ==================================================

# Imports
from time import sleep
from datetime import date

# Funções auxiliares
def linha():
	print('-=' * 20)

# Entrada de dados
linha()
print('\033[1mCLASSIFICANDO ATLETAS\033[m')

linha()
ano_nascimento = int(input('Digite o ano de nascimento: '))

# Processamento
idade = date.today().year - ano_nascimento

linha()
print('ANALISANDO...')
sleep(2)

# Saída de dados
linha()
if idade <= 9:
	print(f'''O atleta tem {idade} anos.
Classificação: MIRIM''')
elif idade <= 14:
	print(f'''O atleta tem {idade} anos.
Classificação: INFANTIL.''')
elif idade <= 19:
	print(f'''O atleta tem {idade} anos.
Classificação: JÚNIOR''')
elif idade <= 25:
	print(f'''O alteta tem {idade} anos.
Classificação: SÊNIOR''')
else:
	print(f'''O atleta tem {idade} anos.
Classificação: MASTER''')


