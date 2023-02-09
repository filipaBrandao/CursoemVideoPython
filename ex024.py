#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
nome = input('Digite uma cidade: ').strip()
a = nome.split()
b = a[0]
c = b.lower()
d = 'santo' in c
print('{}'.format(d))
#ou
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')