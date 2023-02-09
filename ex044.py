# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e sua condição
# de pagamento:
# a vista dinheiro/cheque: 10% de desconto,
# a vista no cartão: 5% de desconto,
# em ate 2x no cartao: preço normal,
# 3x ou mais no cartao: 20% de juros.
vp = float(input('Digite o valor do produto: '))
print('Escolha a forma de pagamento: ')
a = int(input('1-À vista no dinheiro/cheque:\n2-À vista no cartão:\n3-Em até 2x no catão:\n4-3x ou mais no cartão:\n'
              'Qual você prefere?: '))
if a == 1:
    print('Com um desconto de 10% você pagará R${:.2f}'.format(vp - (vp * 0.1)))
elif a == 2:
    print('Com um desconto de 5% você pagará R${:.2f}'.format(vp - (vp * 0.05)))
elif a == 3:
    print('Você pagará o preço normal de R${:.2f}'.format(vp))
elif a == 4:
    print('Com um juros de 20% você pagará R${:.2f}'.format(vp + (vp * 0.2)))
