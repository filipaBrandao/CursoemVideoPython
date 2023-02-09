#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('A média das notas {} e {} é \033[4;37m{}\033[m. \nOu'.format(n1, n2 ,m))
print('A média das notas {:.1f} e {:.1f} é \033[4;37m{:.1f}\033[m'.format(n1, n2 ,m))
