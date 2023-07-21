'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
from datetime import date
nome = str(input('Digite seu nome:')).strip().title()
nascimento = int(input('Digite o ano do seu nascimento:'))
ano = date.today().year
idade = ano - nascimento
if idade >= 3 and idade < 9:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Mirim')
elif idade < 3:
    print('Para começar o treino você precisar ter mais de 3 anos, nesse momento você tem {}!!'.format(idade))
elif idade >= 10 and idade <= 14:
    print('O atleta tem {} anos'.format(idade))
    print('Clissificação: Infantil')
elif idade >= 15 and idade <= 19:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Junior')
elif idade >= 20 and idade <= 25:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Sênior')
else:
    print('O atelta tem {} anos'.format(idade))
    print('Classificação: Master')