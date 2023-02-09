# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela nao pode exeder 30% do salario ou então o emprestimo sera negado,
vc = float(input('Qual o valor da casa que pretende comprar?: '))
sc = float(input('Qual o seu salario?: '))
tp = int(input('Em quantos anos pretende pagar?: '))
a = (vc / tp) / 12
b = sc * 0.3
if a > b:
    print('Emprestimo negado!Você pagaria R${:.2f} por mês.'.format(b))
else:
    print('Seu emprestimo foi aprovado!')
    print('Você pagará R${:.2f} por mês durante {} anos!'.format(a, tp))
