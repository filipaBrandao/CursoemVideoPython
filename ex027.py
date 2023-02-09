#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#Ex: Ana Maria Souza. peimeiro: Ana , ultimo: Souza.
nome = input('Digite seu nome completo: ').strip()
a = nome.split()
print('Primeiro: \033[4;37m{}\033[m'.format(a[0]))
print('Último: \033[4;37m{}\033[m'.format(a[len(a)-1]))
