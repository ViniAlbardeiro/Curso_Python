distancia = float(input('\n Digite a distância da viagem em KM: '))

if distancia >= 200:
    print(f'A viagem custa {distancia * (45/100)} reais.')
else:
    print(f'A viagem custa {distancia * (5/10)} reais.')
