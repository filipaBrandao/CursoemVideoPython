# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.para salarios superiores
# a 1250.00, calcule um aumento de 10%. para inferiores ou iguais, o aumento é de 15%.
a = float(input('Digite seu salario: R$'))
if a > 1250.0:
    print('\033[4mVocê recebera 10% de aumento, seu novo salario é R${:.2f}\033[m'.format(a + (a * 0.1)))
else:
    print('\033[4mVocê recebera 15% de aumento, seu novo salario é de R${:.2f}\033[m'.format(a + (a * 0.15)))
