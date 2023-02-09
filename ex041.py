# A confederação nacional de um atleta de natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria,de acordo com a idade:
# ate 9 anos:mirim,
# ate 14:infantil,
# ate 19:junior,
# ate 20:senior,
# acima:master.
ano = int(input('Qual ano você nasceu? '))
a = 2022 - ano
if a <= 9:
    print('Mirim')
elif a <= 14:
    print('Infantil')
elif a <= 19:
    print('Júnior')
elif a <= 20:
    print('Sênior')
else:
    print('Master')
