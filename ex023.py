#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.Ex digite ym numero:1834
#unidade: 4 dezena: 3 Centena: 8 milhar: 1
n = int(input('Digite um numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: \033[1;37m{}\033[m'.format(u))
print('Dezena: \033[1;37m{}\033[m'.format(d))
print('Centena: \033[1;37m{}\033[m'.format(c))
print('Milhar: \033[1;37m{}\033[m'.format(m))
