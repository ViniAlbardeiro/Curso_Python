marketCar = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor', '4.20',
             'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')

for itemPos in range(0, 18, 2):
    item = marketCar[itemPos]
    price = marketCar[itemPos + 1]
    print(f'{item.ljust(30, ".")} R${ price.rjust(7)}')

l = [0,1,2,3,4,5]
print(len(l))

l.insert(0, [])
print(l)