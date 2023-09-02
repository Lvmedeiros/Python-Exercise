num = (int(input('Digite um valor:')),
int(input('Digite um valor:')),
int(input('Digite um valor:')),
int(input('Digite um valor:')))
print(num)
print(f'O número nove aparece {num.count(9)}')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}')
else:
    print('O número 3 não foi digitado')
print('os valores pares digitados foram:', end=' -> ')
for n in num:
    if n % 2 == 0:
        print(n, end= '')
