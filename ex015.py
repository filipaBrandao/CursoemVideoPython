# Escreva um programa que pergunte a quantidade em Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0.15 por km rodado.
km = float(input('Quantos km esse carro percorreu?'))
da = int(input('Por quantos dias esse carro foi alugado?'))
pda = da * 60
pkm = km * 0.15
pt = pda + pkm
print('\033[1;37mLevando em conta o preço da diaria que ficou por {} e o preço por km rodado que ficou por {}, o preço '
      'total é de {:.2f}\033[m'.format(pda, pkm, pt))
