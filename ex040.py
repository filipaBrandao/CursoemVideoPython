# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final de acordo
# com a media atingida: media abaixo de 5.0: reprovado, entre 5.0 e 6.9: recuperação, 7 ou mais: aprovado.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Reprovado. Sua nota foi {:.1f}'. format(m))
elif m >= 7:
    print('Aprovado. Sua nota foi {:.1f}'. format(m))
else:
    print('Recuperação. Sua nota foi {:.1f}'. format(m))
