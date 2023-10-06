def area(l, c):
    print(f' O terreno com as medidas sendo {l:.2f}x{c:.2f} tem a sua área igual a {(l * c):.2f}m²')


print('Controle de Terreno'.center(60))
print('-'*60)

area(
    float(input(' Largura do terreno (m): ')),
    float(input(' Comprimento do terreno (m): '))
     )
print('~~~~~~')