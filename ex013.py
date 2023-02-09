#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
sa = int(input('Digite seu salario:'))
sn = sa + (sa / 100 * 15)
print('Seu salario com \033[4m15%\033[m de aumento sera de \033[4;37m{}\033[m'.format(sn))