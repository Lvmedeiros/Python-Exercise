'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''
nome = str(input('Digite o seu nome:')).strip()
peso = float(input('Qual é o seu peso:'))
altura = float(input('Qual é a sua altura:'))
imc = peso/ (altura * altura)
print('Olá {}, seja bem-vindo ao Gym Up.'.format(nome))
if imc < 18.5:
    print('Seu IMC é de {:.2f} e você está abixo do peso!'.format(imc))
    print('Está na hora de você comer um pouco mais!')
elif imc < 25:
    print('Seu IMC é de {:.2f} e você está no peso ideal!'.format(imc))
    print('Parabéns!! Continue se alimentando com coisas boas.')
elif imc < 30:
    print('Seu imc é de {:.2f} e você está com sobrepeso! ')
    print('Está na hora de comer menos besteira e fazer exercício.')
elif imc < 40:
    print('Seu imc é de {:.2f} e você está Obesidade!')
    print('Procure fazer mais exercícios e deixe de comer besteira.')
else:
    print('Você está com Obesidade Morbida!')
    print('Procure um médico agora! Você corre sério risco de vida.')