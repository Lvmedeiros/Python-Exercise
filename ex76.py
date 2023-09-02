'''rie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
 mostre uma listagem de preços, organizando os dados em forma tabular.'''
listagem = ('Borracha', 1.50, 'Caderno', 15.00, 'Lapis', 1)
print('-'*40)
print(f'{"LISTA DE COMPRAS":^40}')
print('-'*40)
for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}',end='')
    else:
        print(f'RS${listagem[c]:>7.2f}')