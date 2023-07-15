'''Faça um programa e mostre se ele é Bissexto.'''
from datetime import date
ano = int(input('Que ano quer analizar? Digite 0 para analizar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))

    '''Para um ano ser bissexto ele tem uma regra:
    100 e o resultado não pode ser diferente de zero ou o ano tem que ser divisível 400 e o resultado tem que ser 
    igual a zero '''