nome = input('Digite seu nome:')
salario = float(input('Digite o seu salário atual para ver o seu aumento:'))
n1 = 0.15 * salario
n2 = salario + n1
print('{} o seu novo salário é {}R$ você recebou um aumento de {}R$'.format(nome,n2,n1))