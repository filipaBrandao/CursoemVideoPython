#Desenvolva um programa que pergunte a distancia de um viagem em km. calcule o preco da passagem, cobrando 0.50 por km
#para viagens de ate 200km e 0.45 para viagens mais longas.
a = float(input('Qual é a distancia da sua viagem? '))
print('Você esta prestes a começar uma viagem de {:.2f} km'.format(a))
if a <= 200:
    pr = a * 0.50
else:
    pr = a * 0.45
print('E o preço da sua viagem sera de \033[1;4;37mR${:.2f}\033[m'.format(pr))
