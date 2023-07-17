'''Escreva um programa que leia dois número inteiros e compare-os, mostrando natela uma mensagem.
 - O primeiro valor é maior.
 - O segundo valor é maior
 - Não existe valor maior, os dois são iguais'''
print('Digite dois valores para saber qual é maior.')
n1 = float(input('Digite um valor:'))
n2 = float(input('Digite o segundo valor:'))
if n1 > n2:
    print(' O número {:.2f} é maior que o {:.2f}'.format(n1,n2))
elif n1 < n2:
    print('O número {:.2f} é maior que o {:.2f}'.format(n2,n1))
else:
    print('Não existe valor maior, os dois são iguais.')
