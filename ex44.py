'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''
from time import sleep
print('{:=^40}'.format(' Lojas Medeiros '))
produto = float(input('Valor do Produto:'))
print('Processando a forma de pagamento')
sleep(1)
print('.........')
sleep(2)
print('[1] à vista dinheiro / cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço normal')
print('[4] em até 3 vezes ou mais no cartão: 20% de juros')
num = int(input('Digite uma opção para efetuar o pagamento:'))
if num == 1:
    n1 = produto - (produto * 0.10)
    print('O valor do produto é de R${:.2f}'.format(n1))
elif num == 2:
    n2 = produto - (produto * 0.05)
    print('O valor do seu produto agora é de R${:.2f}'.format(n2))
elif num == 3:
    n3 = produto / 2
    print('Você vai pagar em 2x de R${:.2f} e valor do produto é o mesmo R$ {:.2f}'.format(n3,produto))
elif num == 4:
    parcelas = int(input('Quer pagar em quantas parcelas:'))
    if parcelas >= 3:
        j =  produto * 0.20 * parcelas
        n4 = (j + produto) / parcelas
        total = j + produto
        print(' Você vai pagar 20% juros que  é igual R${:.2f}, o valor total é de R${:.2f} em {} parcelas R${:.2f}'.format(j,total,parcelas,n4))
    else:
        print('Tente outra vez, opção inválida!!')

