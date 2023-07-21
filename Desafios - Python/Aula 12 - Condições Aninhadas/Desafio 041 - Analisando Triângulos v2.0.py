l1 = float(input('Medida do primeiro lado: '))
l2 = float(input('Medida do segundo lado: '))
l3 = float(input('Medida do terceiro lado: '))

if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('\n É possível construir esse triângulo.')

    if l1 == l2 == l3:
        print(' Este triângulo é Equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print(' Este triângulo é Isósceles.')
    else:
        print('  Esse triângulo é Escaleno.')

else:
    print('\n Esse triângulo não existe.')

