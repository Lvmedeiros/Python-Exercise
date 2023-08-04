n1 = int(input('Escolha um número:'))
n2 = int(input('Escolha outro número:'))
opção = 0
while opção != 5:
    print('''[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa''')
    opção =int(input('Qual a sua opção:'))
    if opção == 1:
        n3 = n1 + n2
        print('{} + {} é igual a {}'.format(n1,n2,n3))
    elif opção == 2:
        produto = n1 * n2
        print('{} X {} é igual a {}'.format(n1,n2,produto))
    elif opção == 3:
        if n1 > n2:
            print('O {} é maior que {}'.format(n1,n2))
        else:
            print('o {} é maior que {}'.format(n2,n1))
    elif opção == 4:
        n1 = int(input('Escolha um número:'))
        n2 = int(input('Escolha outro número:'))
    elif opção == 5:
        print('Finalizando....')
    else:
        print('Opção invalida! Tente novamente')
print('Fim do programa! Volte sempre.')

