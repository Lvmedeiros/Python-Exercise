'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
tot = 0
while True:
    jogador = int(input('Escolha um número: '))
    maquina = randint(0, 10)
    total = maquina + jogador
    tipo = ' '
    while tipo not in 'PI':
          tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Jogador jogou {jogador} e máquina jogou {maquina} o resultado é igual {total}')
    print('Deu Par'if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            tot += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
        else:
            print('Você Perdeu!')
            break
    print('Vamos Jogar Novamente?')
print(f'Game Over! Você venceu {tot} vezes.')
