# Escreva um programa  que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário  tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário perdeu ou venceu.
import random
import time
print('-='*20)
print('Vou pensar em um número entre 0 e 5')
print('-=' * 20)
num = int(input('Em que número eu pensei?'))
n3 = random.randint(0,5)
print('Processando ......')
time.sleep(3) # faz com que o computador aguarde 3 segundos
print('O número escolhido foi {} e o número escolhido pelo computador foi {}'.format(num,n3))
if num == n3:
    print('Você ganhou! Parabéns')
else:
    print('Você perdeu! Mais sorte na próxima!')