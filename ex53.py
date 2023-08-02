'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
nome = str(input('Digite uma frase:')).strip().upper()
frase = nome.split()
junto = ''.join(frase)
inverso = ''
'''inverso = junto [::-1] '''#ai não usariamos o for e só o if
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não é um Palíndromo!')
