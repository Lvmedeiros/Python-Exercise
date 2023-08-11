'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
print('Bem vindo a programa de tabuáda')
while True:
    num = int(input('Quer ver a tabuada de qual valor:'))
    print('-'* 40)
    if num >= 0:
        for c in range (1,11):
            mult = c * num
            print(f'{c} X {num} = {mult}')
    else:
        break
print('O programa terminou!')