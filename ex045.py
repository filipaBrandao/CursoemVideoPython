# Crie um programa que faça o computador jogar jokempo com voce.
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('Vamos jogar jokenpô!!!')
a = int(input('''Escolha:
 [ 0 ] pedra
 [ 1 ] papel
 [ 2 ]tesoura
 Qual você quer:'''))
computador = randint(0, 2)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[a]))
if computador == 0:
    if a == 0:
        print('EMPATE')
    elif a == 1:
        print('JOGADOR VENCE')
    elif a == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if a == 0:
        print('COMPUTADOR VENCE')
    elif a == 1:
        print('EMPATE')
    elif a == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if a == 0:
        print('JOGADOR VENCE')
    elif a == 1:
        print('COMPUTADOR VENCE')
    elif a == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
