#Crie um programa que leia quantos dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# 1.00 dolar=3.27 reais
r = float(input('Quantos reais você tem?'))
d = r / 3.27
print('Com R${:.2f} reais você consegue comprar \033[4;37m${:.2f}\033[m dolares'.format(r, d))
#ou
