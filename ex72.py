''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até dez.
Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.'''
cont = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez')
while True:
    num = int(input(' Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        break
    print('Tente novamente!', end='')
print(f'Você digitou o número: {cont[num]}')