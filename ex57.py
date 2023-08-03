'''Faça um programa que leia o sexo de uma pessoa, mas só aceite valores com 'M/F' caso ao contrario ele
peça a digitação novamente.'''
sexo = str(input('Informe seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input('Opção incorreta, por favor digite o sexo [M/F]:')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso'.format(sexo))