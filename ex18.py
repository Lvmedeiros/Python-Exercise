#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math
num = float(input('Digite um ângulo:'))
cos = math.cos(math.radians(num))
tang = math.tan(math.radians(num))
seno = math.sin(math.radians(num))
print('O ângulo escolhido foi {} e valor de Seno {:.2f}, Cosseno {:.2f}, Tangente {:.2f}.'.format(num,seno,cos,tang))