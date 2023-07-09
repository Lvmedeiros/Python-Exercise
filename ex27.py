# Faça o programa que leia o nome completa de uma pessoa e ultimo nome separadamente
n = str(input('Digite seu nomo completo:')).strip().title()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome)-1]))
# para fazer a verificação do último nome tivemos que usar o len , porque ele conta as caracteres ou seja
# entrega o valor total e usamos o -1 .