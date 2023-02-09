#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m**2.
h = float(input('Qual a altura em metros da sua porta?'))
l = float(input('Qual a largura em metros da sua porta?'))
a = h * l
lt = a / 2
print('\033[36mA area da sua porta é de {} e sera necessario {} litros de tinta\033[m'.format(a, lt))
