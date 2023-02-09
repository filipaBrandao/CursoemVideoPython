# Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado: equilatero
# todos os lados iguais, isoceles: dois lados iguais, escaleno: todos os lados diferentes.
a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('\033[1;37mVocê pode fazer um triangulo\033[m')
    if a == b == c:
        print('Será formado um triângulo equilátero.')
    elif a != b != c != a:
        print('Será formado um triângulo escaleno.')
    else:
        print('Será formado um triângulo isoceles.')
else:
    print('\033[1;37mVocê não pode fazer um triangulo\033[m')
