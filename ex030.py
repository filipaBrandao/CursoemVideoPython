#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.
a = int(input('Digite um numero: '))
r = a % 2
if r == 0:
    print('O numero {} é \033[4mPAR\033[m'.format(a))
else:
    print('O numero {} é \033[4mIMPAR\033[m'.format(a))
