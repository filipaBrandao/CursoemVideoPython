# Escreva um programa que leia dois numeros inteiroa e compare-os, mostrando na tela uma mensagem: O primeiro valor
# é maior, o segundo valor é maior, não existe valor maior, os dois são iguais.
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))
if v1 > v2:
    print('O primeiro valor é maior!')
elif v2 > v1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais.')
