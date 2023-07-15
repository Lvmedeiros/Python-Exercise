#Digite 3 valores na tela e mostre qual é o maior e qual é o menor
a = float(input('Digite um valor:'))
b = float(input('Digite um segundo valor:'))
c = float(input('Digite o segundo valor:'))
# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi : {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))

