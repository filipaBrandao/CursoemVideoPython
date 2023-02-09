# Faça um programa que calcule entre todos os numeros impares que sao multiplos de tres e que se incontram no
# intervalo de 1 ate 500.
d = 0
e = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        e = e + 1
        d = d + c
print('A soma de todos os {} valores é de {}'.format(e, d))

print('FIM!!!')
