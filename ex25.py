# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome.
nome = str(input('Digite seu nome:')).strip().title()
print('Seu nome tem Silva? {}'.format('Silva' in nome))
print(nome)

# Na resolução do exercício, o professor usou .upper ou .lower e não usou .title, mas como estamos falando de
# nome e se tivessemos que escrever ele na tela nada melhor do que ele aparecer da forma correta! Então pode até
# digitar o nome errado que o programa vai devolver um print do seu nome corretamente!