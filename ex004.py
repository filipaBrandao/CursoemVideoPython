#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis
#sobre ele.
n = input('Digite algo:')
print('\033[35m-=\033[m' * 20)
print('O tipo primitivo desse valor é', type(n))
print('É alfa?', n.isalpha())
print('maiusculas?', n.isupper())
print('É um alfanumerico?', n.isalnum())
print('ascii?', n.isascii())
print('decimal?', n.isdecimal())
print('digito?', n.isdigit())
print('identifier?', n.isidentifier())
print('minuscula', n.islower())
print('pritable', n.isprintable())
print('So tem espaços?', n.isspace())
print('capitalizada?', n.istitle())
print('\033[35m-=\033[m' * 20)
