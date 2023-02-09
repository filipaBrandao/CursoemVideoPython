#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('\033[1;37mVocê pode fazer um triangulo\033[m')
else:
    print('\033[1;37mVocê não pode fazer um triangulo\033[m')
