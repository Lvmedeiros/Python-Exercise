#Faça um programa que leia algo pelo teclado e mostra o seu tipo primitivo e todas as informações
#possíveis sobre ele
a = input('Type something:')
print('O tipo premitivo desse valor é :{}'.format(type(a)))
print('Só tem espaços: {}'.format(a.isspace()))
print('O que você digitou é capitalizado: {}'.format(a.istitle()))
print('É um número: {}'.format(a.isnumeric()))
print('É alpha numérico: {}'.format(a.isalnum()))
print('É alfabético: {}'.format(a.isalpha()))
print('Tudo é letras minusculas: {}'.format(a.islower()))
print('Esta tudo em letras maiusculas: {}'.format(a.isupper()))