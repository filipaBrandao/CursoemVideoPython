# Melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 e 10.
# so que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios
# para vencer.
from random import randint
from time import sleep
'''a = randint(0, 10)
c = 0
print('\033[33m-=-\033[m' * 20)
print('Estou pensando em um numero, tente adivinhar')
print('\033[33m-=-\033[m' * 20)
while c != a:
    c = int(input('Digite um número entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(0.5)
    if c != a:
        print('Você perdeu, eu pensei no numero {}. Tente novamente!'.format(a))
if c == a:
   print('Você venceu, eu pensei no numero {}!!'.format(a))'''
computador = randint(0, 10)
print('Sou seu computador, acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente ,mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabens!'.format(palpites))
