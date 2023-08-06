'''perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer
 mostrar 0 termos.'''
print('Gerador de PA')
print('-' * 20)
primeiro = int(input('Digite o termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
termo = primeiro
cont= 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
        print('Puasa')
        mais = int(input('Quantos termos você quer mostrar a mais: '))
print('Final da prograssão com {} termos.'.format(total))


