dias = float(input('Por quantos dias você alugou o carro:'))
km = float(input('Quantos Km você rodou com o carro:'))
n1 = dias * 60
n2 = km * 0.15
n3 = n1 + n2
print('O valor do Km {}R$ e o valor do aluguel do carro {}R$'.format(n1,n2))
print('O valor total a se pagar pelo aluguel e pelo Km são {}R$'.format(n3))