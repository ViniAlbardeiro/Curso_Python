speed = float(input('\n Digite a velocidade registrada: '))

if speed > 80:
    print(f'Você ultrapassou o limite de velocidade de 80KM/h, logo, levará uma multa de {(speed-80)*7} reais.')
else:
    print('Parabéns, você é um cidadão responsável!')
