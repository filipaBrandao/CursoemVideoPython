#Escreva um programa que leia a velocidade de um carro. Se ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
#multado, a multa vai custar 7,00 por cada km acima do limite.
v = float(input('Digite a velocidade em km do carro: '))
if v > 80:
    a = v - 80
    b = a * 7
    print('Você foi multado! O limite de velocidade é 80km/h \nO valor a pagar é de \033[1;4;37mR${:.2f}\033[m'.format(b))
print('Tenha um bom dia, dirija com segurança!')
