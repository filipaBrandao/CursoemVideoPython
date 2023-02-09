# Desenvolva uma logica que leia o peso e uma altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com
# a tabela abaixo,
# abaixo de 18.5: abaixo do peso,
# entre 18.5 e 25: peso ideal,
# 25 ate 30: sobrepeso,
# 30 ate 40:obesidade,
# acima de 40: obesidade morbida.
pe = float(input('Quanto você pesa? '))
al = float(input('Qual a sua altura? '))
a = pe / (al * al)
if a < 18.5:
    print('Abaixo do peso.')
elif a < 25:
    print('Peso ideal.')
elif a < 30:
    print('Sobrepeso.')
elif a < 40:
    print('Obesidade.')
elif a >= 40:
    print('Obesidade morbida.')
