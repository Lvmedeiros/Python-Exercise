'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
 os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
 continuar a digitar valores.'''
r = 'S'
soma = cont = media = maior = menor = 0
r = str(input('Quer continuar [S/N]:')).strip().upper()[0]
while r in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer continuar [S/N]:')).strip().upper()[0]
media = soma / cont
print(' A media de todos os valores é {} o maior número foi {} e o menor foi {}'.format(media,maior, menor))