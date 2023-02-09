# Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente ate ter um valor correto.
r = str(input('Qual seu gênero? \033[37m[F/M]:\033[m ')).upper().strip()[0]
while r not in 'MF':
        print('\033[33mInválido\033[m')
        r = str(input('Digite novamente \033[37m[F/M]:\033[m '))
print('Fim!!!')
