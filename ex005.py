#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um numero'))
a = n - 1
s = n + 1
print('\033[1;36mO antecessor do numero {} é {} e seu sucessor é {}\033[m \n ou'.format(n, a, s))
#ou
print('\033[1;34mO antecessor do numero {} é {} e seu sucessor é {}\033[m'.format(n, (n-1),(n+1)))