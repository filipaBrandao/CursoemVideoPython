#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
nome = input('Digite seu nome: ').strip()
a = nome.upper()
b = 'SILVA' in a
print('{}'.format(b))
#ou
nome = str(input('Digite seu nome: ').strip())
print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))
