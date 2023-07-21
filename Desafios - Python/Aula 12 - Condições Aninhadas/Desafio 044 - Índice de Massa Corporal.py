from math import pow

m = float(input('\n Digite seu peso(Kg): '))
a = float(input(' Digite sua altura(m): '))
imc = m / pow(a, 2)

if imc < 18.5:
    print(' Você está abaixo do peso ideal.')

elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')

elif 25 <= imc < 30:
    print('Você está no estado de sobrepeso.')

elif 30 <= imc < 40:
    print(' Você está obeso.')

elif imc >= 40:
    print('Você está na classe obesidade mórbida.')
