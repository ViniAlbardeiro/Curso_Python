from math import hypot

ctop = float(input('\n Digite a medida do cateto oposto: '))
ctad = float(input('Digite a medida do cateto adjacente: '))

print(f'\n A medida da hipotenusa é: {hypot(ctop, ctad)}')
