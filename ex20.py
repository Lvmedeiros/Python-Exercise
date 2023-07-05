#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = input('Digete o nome do primeiro aluno:')
n2 = input('Digite o nome do Seugundo aluno:')
n3 = input('Digite o nome do Terceiro Aluno ')
n4 = input('Digite o nome do quarto aluno:')
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A sequência de apresentação do trabalho é')
print(lista)