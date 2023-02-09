#Crie um programa que leia dois numeros e mostre a soma entre eles.
n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro numero'))
s = n1 + n2
print('A soma entre \033[33m{}\033[m e \033[34m{}\033[m é \033[1;32m{}\033[m'.format(n1, n2, s))