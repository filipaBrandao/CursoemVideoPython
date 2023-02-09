# Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar, desconcidere-o.
b = 0
d =0
for c in range(0, 6):
    a = int(input('Digite um numero: '))
    if a % 2 == 0:
        b += a
        d += 1
print('A soma dos {} valores pares é {}'.format(d, b))
