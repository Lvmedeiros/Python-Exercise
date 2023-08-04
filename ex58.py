'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
print('----- Bem-Vindo ao Jogo de adivinha -----')
nome = str(input('Digite seu nome:')).strip().title()
n1 = str(input('Olá {},sa quer continuar? [S/N]:'.format(nome))).strip().upper()[0]
if n1 in 'Ss':
    escolha = randint(0,10)
    num = int(input('Escolha um nmero entre 0 a 10:'))
    print('anlisando a escolha...')
    sleep(1)
    print('.....')
    while num != escolha:
        print('Você perdeu,mais sorte na próxima!')
        print('-----------')
        num = int(input('Escolha outro número:'))
        if num == escolha:
            print('Prabéns {} você ganhou!'.format(nome))
else:
    print('O jogo terminou!!')
    print('----------------')
    n2 = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if n2 in 'Ss':
        escolha = randint(0, 10)
        num = int(input('Escolha um nmero entre 0 a 10:'))
        print('anlisando a escolha...')
        sleep(1)
        print('.....')
        while num != escolha:
            print('Você perdeu,mais sorte na próxima!')
            print('-----------')
            num = int(input('Escolha outro número:'))
            if num == escolha:
                print('Prabéns {} você ganhou!'.format(nome))

