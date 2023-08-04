from random import randint
computador = randint(0,10)
print('Sou seu computador e acabei de pensar em um número de 0 a 10.')
print('Será que consegue adivinhar qual foi:')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('qual é o seu palpite?'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou {} com tantos palpites.'.format(palpite))

