nome = input('Digite seu nome:')
largura = float(input('Digite quantos metros de largura tem sua parade:'))
altura = float(input('Digite quantos metros de altura tem sua parade:'))
area =  largura * altura
tinta = area / 2
print('{} sua parade tem {}m² e você precisara de {} litros de tinta.'.format(nome,area,tinta))