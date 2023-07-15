# Desenvolva um programa que pergunte uma distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$ 0,50 por uma viagem de até 200 Km e R$ 0,45 para viagens mais longas.
cidade = str(input('Qual o nome da cidade que você vai viajar:'))
n1 = float(input('Quantos Km tem a sua viagem:'))
n2 = n1 * 0.50
n3 = n1 * 0.45
if n1 <= 200:
    print('O valor da sua viagem para {} é de R$ {:.2f}. '.format(cidade,n2))
else:
    print('O valor da sua viagem para {} é de R$ {:.2f}'.format(cidade,n3))