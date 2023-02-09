# Refaça o exercicio 009, mostrando a tabuada que o usuario escolher, so que agora utilizando um laço for.
a = int(input('Qual tabuada voce quer? '))
for c in range (0, 11):
    b = a * c
    print('{} x {:2} = {:2}\n'.format(a, c, b))
