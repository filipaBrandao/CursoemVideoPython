# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.ex:Digite um
# numero: 6.127. O numero 6.127 tem a parte inteira 6.
from math import trunc
n = float(input('Digite um valor: '))
print(f'O valor digitado foi \033[36m{n}\033[m e a sua porção inteira é \033[34m{trunc(n)}\033[m')
