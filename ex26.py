# Faça um programa que leia uma frase pelo teclado e mostre 'A'
#Quantas vez aparece a letra 'a'
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece na ultima Vez
frase = str(input('Escreva uma frase:')).strip().upper()
print('A letra (a) aparece:{}'.format(frase.count('A')))
print('A letra (a) aparece pela primeira vez na posição: {}'.format(frase.find('A')+1))
print('A última letra (a) apareceu na posição: {}'.format(frase.rfind('A')+1))
# Para começarmos a contar do 1 em diante e não do 0 igual o python faz. us