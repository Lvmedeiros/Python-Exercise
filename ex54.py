'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for c in range (1, 8):
    n1 = int(input('Em que ano a {}ª pessoa nasceu:'.format(c)))
    data = ano - n1
    if data >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Tivemos {} pessoas maiores de idade e tivemos {} menores de idades.'.format(totmaior,totmenor))
