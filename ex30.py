# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
num = int(input('Digite um número inteiro para saber se ele é par ou impar:'))
resultado = num % 2 # usamos % que no python é o resto da divisão porque to-do número par da zero!
if resultado == 0:
    print('O número {} é Par!'.format(num))
else:
    print('O número {} é Impar'.format(num))
