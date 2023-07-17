'''Escrva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''
num = int(input('Digite um número inteiro:'))
print('''[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
escolha = int(input('Sua opção:'))
if escolha == 1:
    print('O número escolhido foi {} e a transformação para Binario é {}'.format(num,bin(num)[2:]))
elif escolha == 2:
    print('O número escolhido foi {} e a transformação para Octal é {} '.format(num,oct(num)[2:]))
elif escolha == 3:
    print('O número escolhido foi {} e a transformação para Hexadecimal é {}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida! Tente novamente.')
# usamos [2:] para iniciar a partir casa némero 2 técnica de fatiamento.