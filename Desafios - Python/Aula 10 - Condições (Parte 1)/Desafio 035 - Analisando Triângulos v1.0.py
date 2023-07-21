lado1 = float(input('\n Digite a primeira medida do triângulo:'))
lado2 = float(input('\n Digite a segunda medida do triângulo:'))
lado3 = float(input('\n Digite a terceira medida do triângulo:'))

if lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado2+lado3 > lado1:
    print('\n\n  É possível criar esse triângulo.')
else:
    print('\n\n  Não é possível criar esse triângulo.')