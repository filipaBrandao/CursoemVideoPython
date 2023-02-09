#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule
# e mostre o comprimento da hipotenusa
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir \033[32m{:.2f}\033[m.'.format(hi))