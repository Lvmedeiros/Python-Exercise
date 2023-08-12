'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
print('-' * 20)
n1 = 'Lojas Medeiros'
print(f'{n1:^20}')
print('-' * 20)
tot = produtomaior1000 = menor = cont = 0
nprodutomaisbarato = ' '
while True:
    produto = str(input('Digite o nome do produto: ')).strip().title()
    valor = float(input('Preço:R$ '))
    tot += valor
    cont += 1
    if valor >= 1000:
        produtomaior1000 += 1
    if cont == 1:
        menor = valor
        nprodutomaisbarato = produto
    else:
        if valor < menor:
            menor = valor
            nprodutomaisbarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DE JOGO '))
print(f'O total gasto na compra é de R$ {tot:.2f}')
print(f'O total de produtos com valor acima de R$1000 são: {produtomaior1000}')
print(f'O nome do produto mais barato é {nprodutomaisbarato} e seu valor é R$ {menor}')
