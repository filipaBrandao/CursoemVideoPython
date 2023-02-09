#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
po = float(input('Digite o preço original:'))
pd = po - (po * 0.05)
print('O novo preço do produto é de \033[4;37m{:.2f}\033[m reais'.format(pd))