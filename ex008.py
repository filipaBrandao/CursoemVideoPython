#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
me = float(input('Digite uma quantidade em metros:'))
ce = me * 100
mi = me * 1000
print('\033[33m-+\033[m' * 40)
print('{} metros são iguais a {} centimetros ou a {} milimetros'.format(me, ce, mi))
print('\033[33m-+\033[m' * 40)