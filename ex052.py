# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
a = int(input('Digite um numero: '))
b = 0
for c in range(1, a + 1):
    if a % c == 0:
        print('\033[33m', end=' ')
        b += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m\nO numero {} foi divisivel {} vezes'.format(a, b))
if b == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele nao é primo')
