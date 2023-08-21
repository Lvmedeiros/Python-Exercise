'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Cuiabá.'''
times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Grêmio', 'Flamengo', 'Bragantino',
         'Atlhetico-PR', 'Fortaleza', 'Cuiabá', 'São Paulo', 'Atlético-Mg',
         'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos',
         'Coritiba', 'Vasco da Gama', 'América Mineira')
a = times[0:5]
b = times[-5:]
print(f'Os 5 primeiro times são:{a} ')
print(f'Os 5 últimos colocados são: {b}')
print(f'Os times em ordem alfabética são:{sorted(times)}')
print('O Cuiabá está na posição {}'.format(times.index("Cuiabá")))

