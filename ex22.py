#crie um programa que leia o nome de uma pessoa e mostre:
# O nome com todas as letras em maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo sem considerar espaço
# Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome em letra maiúscula é {}.'.format(nome.upper()))
print('Seu nome em letre minúscula é {}.'.format(nome.lower()))
print('Seu nome tem {} letras ao todo.'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome ao todo tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

# Usamos o strip logo na primeira linha código para tirar os espaços antes e os espaços que podem ser
# colocados depois. e pra eliminar o do meio usamos - nome.count(' ')