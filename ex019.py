#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido.
from random import choice
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
lista = [pa, sa, ta, qa]
e = choice(lista)
print('O aluno escolhido foi \033[4;1;37m{}\033[m.'.format(e))
