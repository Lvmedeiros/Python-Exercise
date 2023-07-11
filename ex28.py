# Escreva um programa  que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário  tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário perdeu ou venceu.
import random
num = float(input('Escolha um número entre 0 e 5 :'))
lista = [0,1,2,3,4,5]
n3 = random.choice(lista)
print('O número escolhido foi {} e o número sorteado foi {}'.format(num,n3))
if num == n3:
    print('Você ganhou! Parabéns')
else:
    print('Você perdeu! Mais sorte na próxima!')