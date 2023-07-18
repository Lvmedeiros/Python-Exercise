'''Crie um programa que leia duas notas de um aluno e calcule sua média,mostrando uma mensagem
no final, de acordo com a média atingida:'''
nome = str(input('Digite o seu nome:')).strip().title()
n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite a sua segunda nota:'))
media = (n1+n2) / 2
if media >= 6 and media < 10:
    print('{} sua média é {:.2f}'.format(nome,media))
    print('Você foi aprovado!!')
elif media < 6 and media > 4.5:
    print('{} você está de recuperação!! Sua média foi {:.2f}'.format(nome, media))
elif media > 10:
    print('A média nessa escola é superior as das escolas tradicionais. Sua média foi {:.2f}'.format(media))
else:
    print('Você foi reprovado!!')