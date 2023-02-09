# Refaça o desafio 051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros termos da progressao
# usando a estrutura while.
'''a = int(input('Inicio: '))
b = int(input('Passo: '))
c = 1
d = a
while c <= 10:
    d = a + (10 - 1) * b
    print(d, end=' ')
    c = c + 1
print('Fim')
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{}, '.format(termo), end=' ')
    termo += razao
    cont += 1
print('Fim')
