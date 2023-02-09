# Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior,
# [ 4 ] novos numeros, [ 5 ] sair do programa.Seu programa devera realizar a operação solicitada em cada caso.

c = 0
d = ''
a = int(input('Digite um valor: '))
b = int(input('Digite mais um valor: '))
if a > b:
    d = a
else:
    d = b
while c != 5:
    c = int(input('''-------------MENU-------------
    [ 1 ]Somar
    [ 2 ]Multiplicar
    [ 3 ]Maior
    [ 4 ]Novos valores
    [ 5 ]Sair do programa
    Digite um numero: '''))
    if c == 1:
        print('{} + {} = {}'.format(a, b, a + b))
    elif c == 2:
        print('{} x {} = {}'.format(a, b, a * b))
    elif c == 3:
        if a == b:
            print('Os numeros {} e {} são iguais.'.format(a, b))
        else:
            print('Entre {} e {} o maior número é {}'.format(a, b, d ))
    elif c == 4:
        print('Novos numeros: ')
        a = int(input('Digite um valor: '))
        b = int(input('Digite outro valor: '))
print('\033[31mFim\033[m')
