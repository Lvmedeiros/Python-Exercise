# Escreva um programa que leia a valocidade de um carro.
# Se ele ultrappassar 80Km/h, mostra uma mensagem dizendo  que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite .
n1 = float(input('Qual a velocidade do seu carro:'))
n2 = (n1 - 80)*7
if n1 <= 80:
    print('Você está conduzindo em segurança! Parabéns!')
else:
    print('Você foi multado! O valor da multa é de R$ {}'.format(n2))