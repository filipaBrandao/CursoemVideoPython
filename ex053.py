# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# apos a sopa (da pra ler de tras pra frente que é a mesma coisa sem contar espaços)
a = (input('Digite uma frase: ')).strip().lower()
b = a.split()
c = ''.join(b)
d = ''
d = c[::-1]
'''for f in range(len(c) - 1, -1, -1):
    d += c[f]'''
if c == d:
    print('É um palindromo')
else:
    print('Não é um palindromo')
