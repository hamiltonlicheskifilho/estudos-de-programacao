# ==================================================
# Exercício: Reajuste Salarial
# Objetivo: ler o salário de um funcionário
# e mostrar o novo valor com 15% de aumento
# ==================================================

# Entrada de dados
salario_funcionario = float(input('Digite o salário do funcionário: R$ '))

# Processamento
# Duas formas de calcular o aumento (optei pela porcentagem explícita)
aumento_salario = salario_funcionario + (salario_funcionario * 15 / 100)

# Saída de dados
print(
    f'O salário do funcionário era R$ {salario_funcionario:.2f} '
    f'e, após um aumento de 15%, passou a ser R$ {aumento_salario:.2f}.'
)