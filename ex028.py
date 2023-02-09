# Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir
# qual foi o numero escolhido pelo computador.(o programa devera escrever na tela se o usuario venceu ou perdeu.
from random import randint
from time import sleep
a = randint(0, 5)
print('\033[33m-=-\033[m' * 20)
print('Estou pensando em um numero, tente adivinhar')
print('\033[33m-=-\033[m' * 20)
c = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if c == a:
    print('Você venceu, eu pensei no numero {}!!'.format(a))
else:
    print('Você perdeu, eu pensei no numero {}!'.format(a))
