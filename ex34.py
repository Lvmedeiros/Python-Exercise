#Escreva um programa que pergunte o valor do sário de um funcionário e calcule o valor do aumento
# Para salários inferiores a 1250 15% de aumento para salários superiores 10%
nome = str(input('Digite seu nome:'))
salario = float(input('Digite o valor do seu salário para saber o seu aumento:'))
if salario > 1250:
    aumento = (salario * 0.10)
    n1 = salario + aumento
    print('Você recebera R$ {:.2f} e o seu aumento foi de R% {:.2f}.'.format(n1, aumento))
else:
    if salario <= 1250:
        aumento= (salario * 0.15)
        n1 = salario + aumento
        print('Você recebera R$ {:.2f} e seu aumento foi de R% {:.2f}.'.format(n1,aumento))
