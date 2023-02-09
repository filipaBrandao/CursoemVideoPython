# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se
# alistar ao serviço militar, Se é a hora de ele se alistar, se ja passou do tempo do alistamento, seu programa
# tambem devera mostrar o tempo que falta ou que passou do prazo.
i = int(input('Data de nascimento? '))
a = 2022 - i
if a < 18:
    print('Ainda faltam {} anos para se alistar.'.format(18 - a))
elif a > 18:
    print('Ja passou {} anos do seu alistamento.'.format(a - 18))
else:
    print('Esta na hora de você se alistar.')
