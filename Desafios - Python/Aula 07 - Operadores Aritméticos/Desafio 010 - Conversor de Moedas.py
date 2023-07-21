print('Conversor de Real para Dólar.\n')

r = float(input('Coloque a quantia de dinheiro que você tem disponível: '))
d = float(input('Coloque a cotação do Dólar Americano para Real Brasileiro: '))
print(f'\nCom o dólar custando R${d:.2f}, você teria disponível ${r / d:.2f}')
