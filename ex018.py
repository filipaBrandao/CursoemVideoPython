#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo de {} tem o \033[1mSENO\033[m de {:.2f} \nO ângulo de {} tem o \033[1mCOSSENO\033[m de {:.2f} \nO ângulo '
      'de {} tem a \033[1mTANGENTE\033[1m de {:.2f}'.format(a, s, a, c, a, t))
