'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep
n = int(input('Digite um valor para ver a sua contagem regressiva:'))
for c in range (n, -1, -1):#para ele contar até zero o final tem que ser menos -1, se for 0 ele conta até 1
    print(c)
    sleep(1)
print('Feliz Ano Novo!')