#O mesmo professor so desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('Ordem de apresentação sera')
print('\033[33m-+\033[m' * 20)
print(lista)
print('\033[33m-+\033[m' * 20)
