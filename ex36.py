'''Escreva um programa para aprovar um impréstimo banário para a compra de uma casa. o programa
vai perguntar o valor da casa, o valor do salário do comprador  e em quantos anos ele vai pagar .
Calcule o valor da da prestação  mensal , sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado.'''
nome = str(input('Digite o nome do comprador:')).strip().title()
salário = float(input('Qual é o salário do {}:'.format(nome)))
casa = float(input('Qual é o valor da casa R$:'))
anos = float(input('Quantos anos o {} vai parcelar:'.format(nome)))
prestação = casa / (anos * 12)
mínimo = salário * 0.30
print('Para pagar o valor da casa R$ {:.2f} em {} anos'.format(casa,anos), end=' ')
print('A prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Parabêns {} o seu empréstimo foi aprovado!!'.format(nome))
else:
    print('Empréstimo negado!')