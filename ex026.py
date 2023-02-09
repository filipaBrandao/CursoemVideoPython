#Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra 'a', em que posição ela
#aparece a primeira vez, em que posição ela aparece a ultima vez.
frase = input('Digite uma frase: ').lower().strip()
a = frase.count('a')
print('A letra a aparecem \033[1m{}\033[m vezes na frase {}.'.format(a, frase))
b = frase.find('a') + 1
print('O primeiro a aparece na posição \033[1m{}\033[m'.format(b))
c = frase.rfind('a') + 1
print('O ultimo a aparece na posição \033[1m{}\033[m'.format(c))
#ou
frase = input('Digite uma frase: ').upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
