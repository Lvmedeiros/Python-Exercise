'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no
intervalo de 1 até 500.'''
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c # soma todos os valores
        cont += 1 # += É igual a linha 7 mais simplificado, e aqui ele conta os números somados.
print('A soma de todos os {} valores solicitador é {}'.format(cont,soma))
