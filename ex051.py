# Desenvolva um programa que leia o primeiro termo e a razao de uma progressao aritmetrica. No final, mostre os 10
# primeiros termos dessa progressao.
a = int(input('Inicio: '))
d = int(input('Passo: '))
b = a + (11 - 1) * d
for c in range(a, b, d):
    print(c, end=' ')
print('FIM!!!')
