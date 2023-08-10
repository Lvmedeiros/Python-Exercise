'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
 o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
eles (desconsiderando o flag).'''
num = 0
soma = 0
tot = 0
num = int(input('Digite um número [999 para  parar]: '))# colocamos aqui para  não fazermos o formate com (soma - 999)
# e (tot - 1)
# num = soma = tot = 0 (posso representar dessa forma também)
while num != 999:
    num = int(input('Digite um número [999 para  parar]: '))
    soma += num
    tot += 1
print('Você digitou {} número e soma deles é {}'.format(tot,soma)) #tot - 1 e soma - 999 explicação acima!