'''Faça um programa que leia a idade de um jovem e informe, de acordo com sua idade, se ele ainda
vai se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo
que falta ou se já passou do prazo.'''
from datetime import date
import time
nome = str(input('Digite o seu nome:')).strip().title()
data = int(input('Em que ano você nasceu:'))
ano = date.today().year
alistamento = ano - data
print('Analisando os dados de alistamento')
time.sleep(2)
print('.......')
time.sleep(3)
print('{} nasceu  em {} e tem {} anos em {}'.format(nome,data,alistamento,ano))
if alistamento == 18:
    print('Está na hora de se alistar, você já tem {} anos '.format(alistamento))
elif alistamento == 17:
    print('Faltam 1 ano para o seu alistamneto')
elif alistamento < 17:
    n1 = 18 - alistamento
    print('Falta {} anos para o seu alistamento'.format(n1))
elif alistamento == 19:
    print('Já passou do tempo de alistamento há 1 ano')
else:
    n2 = alistamento - 18
    print('Já passou do tempo de alistamento  há {} anos '.format(n2))



