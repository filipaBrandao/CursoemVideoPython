# Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.
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
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}, '.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
