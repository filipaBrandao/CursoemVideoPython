# Inserir um nome completo e mostrar ele maiusculo, minusculo, contar quantos caracteres tem sem os espaços e quantas
#letras tem o primeiro nome
nome = input('Digite seu nome completo: ').strip()
ma = nome.upper()
print('Maiusculo: \033[4;37m{}\033[m'.format(ma))
mi = nome.lower()
print('Minúsculo: \033[4;37m{}\033[m'.format(mi))
s = nome.split()
j = ''.join(s)
l = len(j)
print('Seu nome tem um total de \033[4;37m{}\033[m letras.'.format(l))
f = nome.split()
pn = f[0]
lp = len(pn)
print('Seu primeiro nome tem \033[4;37m{}\033[m letras.'.format(lp))
 #ou
nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é \033[4;37m{}\033[m'.format(nome.upper()))
print('Seu nome em minúsculo é \033[4;37m{}\033[m'.format(nome.lower()))
print('Seu nome tem ao ao todo \033[4;37m{}\033[m letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem \033[4;37m{}\033[m letras'.format(nome.find(' ')))
