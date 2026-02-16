# ==================================================
# Exercício: Analisando Triângulos
# Objetivo: Ler o comprimento de três retas e diga ao 
# usuário se elas podem ou não formar um triângulo e 
# mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
# ==================================================

# Imports
from time import sleep

# Funções auxiliares
def linha():
    print('-=' * 30)

# Entrada de dados
linha()
print('\033[1mANALISANDO TRIÂNGULOS v2.0\033[m')
linha()

p1 = int(input('Primeiro segmento: '))
p2 = int(input('Segundo segmento: '))
p3 = int(input('Terceiro segmento: '))

linha()
print('\033[1mANALISANDO...\033[m')
sleep(2)

# Processamento
linha()
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmentos PODEM formar um TRIÂNGULO')

    if p1 == p2 == p3:
        print('Tipo: \033[1mEQUILÁTERO\033[m')
    elif p1 == p2 or p1 == p3 or p2 == p3:
        print('Tipo: \033[1mISÓSCELES\033[m')
    else:
        print('Tipo: \033[1mESCALENO\033[m')
else:
    print('Os segmentos NÃO PODEM formar um TRIÂNGULO')
