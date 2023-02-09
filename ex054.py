# Crie um programa que leia o ano de nascimento de 7 pessoas.No final, mostre quantas pessoas ainda não atinjiram a
# maioridade e que quantos ja são maiores.
'''ma = []
me = []
for c in range(0, 7):
    a = int(input('Ano de nascimento: '))
    b = 2022 - a
    if b >= 18:
        ma.append(b)
    else:
        me.append(b)

print('Tem {} pessoas de maior.'.format(len(ma)))
print('Tem {} pessoas de menor'.format(len(me)))'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo temos {} pessoas maiores de idade'.format(totmaior))
print('E {} menor de idade'.format(totmenor))
