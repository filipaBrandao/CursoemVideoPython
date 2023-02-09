#Escreva um programa que converta uma temperatura digitando em graus celsios e converta para graus fahrenheit.
c = float(input('Quantos graus celsios estao fazendo?'))
f = c * 1.8 + 32
print('{} graus celsios são iguais à \033[4;37m{} graus fahrenheit\033[m'.format(c, f))
