# ==================================================
# Exercício: Calculadora IMC
# Objetivo: Ler o peso e altura de uma pessoa, calcular
# seu Índice de Massa Corporal (IMC) e mostrar seu 
# status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
# ==================================================

# Imports
from time import sleep

# Funções auxiliares
def linha():
	print('-=' * 30)


# Entrada de dados
linha()
print('\033[1mÍNDICE DE MASSA CORPORAL\033[m')
linha()

weight = float(input('Digite seu peso: '))
height = float(input('Digite sua altura: '))

# Processamento
imc = weight / (height ** 2)

linha()
print('\033[1mANALISANDO...\033[m')
sleep(2)
linha()

# Saída de dados
if imc < 18.5:
	print(f'''O seu IMC é de {imc:.1f}.
Você está na faixa de PESO: \033[1mABAIXO DO PESO\033[m''')
elif imc < 25:
	print(f'''O seu IMC é de {imc:.1f}.
Você está na faixa de PESO: \033[1mIDEAL\033[m''')
elif imc < 30:
	print(f'''O seu IMC é de {imc:.1f}.
Você está na faixa de PESO: \033[1mSOBREPESO\033[m''')
elif imc < 40:
	print(f'''O seu IMC é de {imc:.1f}.
Você está na faixa de PESO: \033[1mOBESIDADE\033[m''')
else:
	print(f'''O seu IMC é de {imc:.1f}.
Você está na faixa  de PESO: \033[1mOBESIDADE MÓRBIDA\033[m''')