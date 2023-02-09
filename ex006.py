#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um numero:'))
d = n * 2
t = n * 3
r = n ** (1/2)
c = {'li': '\033[m',
     'br': '\033[1;97m',
     'am': '\033[0;33m',
     'vr': '\033[0;32m',
     'ac': '\033[0;36m'}

print('O dobro de {}{}{} é {}{}{}, seu triplo é {}{}{} e sua raiz quadrada é {}{:.2f}{}. \nOu'
      .format(c['br'], n, c['li'],c['am'] , d, c['li'], c['vr'], t, c['li'], c['ac'] , r, c['li'],))
print('O dobro de {}{}{} é {}{}{}, seu triplo é {}{}{} e sua raiz quadrada é {}{:.2f}{}. \nOu'
      .format(c['br'], n, c['li'], c['am'] , (n * 2), c['li'], c['vr'],(n * 3), c['li'], c['ac'],(n ** (1/2)), c['li']))
print('O dobro de {}{}{} é {}{}{}, seu triplo é {}{}{} e sua raiz quadrada é {}{:.2f}{}.'
      .format(c['br'], n, c['li'],c['am'] , (n * 2), c['li'], c['vr'],(n * 3), c['li'],c['ac'] , pow(n,(1/2)), c['li'],))