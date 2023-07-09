# Crie um programa que leia e diga se a sua cidade começa com o nome 'SANTO'
#cidade = str(input('Qual cidade você nasceu:')).title().strip()
#print('Santo'in cidade)
cid = str(input('Qual cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')