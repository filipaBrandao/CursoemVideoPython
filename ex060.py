# Faça um programa que leia um numero qualquer e mostre o seu fatorial. Ex: 5! = 5*4*3*2*1 = 120
'''from math import factorial
n = int(input('Digite um numero: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

n = int(input('Digite um numero: '))
c = n
f = 1
print('Calculando {}! ='.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else  '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))
