'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:'''
tot18 = toth = totm20 = 0
while True:
    n1 = 'Cadastre uma pessoa'
    print('-' * 40)
    print(f'{n1:^40}')
    print('-' * 40)
    idade = int(input('Qual é a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 +=1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'O total de pessoas maiores idade: {tot18}')
print(f'Total de homens presente: {toth}')
if totm20 == 1:
    print('Neste momento existe ao todo 1 mulher menor de 20 anos ')
elif totm20 == 0:
    print('Neste momento existe ao todo 0 mulheres menores de 20 anos ')
else:
    print(f'O total de mulheres é igual: {totm20}')