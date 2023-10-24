

def fatorial(num, calc):
    multiply = 1
    print('__'*35)
    print(f'{num}!', end=" = ")
    for numero in range(num, 1, -1):
        multiply *= numero
        if calc in "SS:":
            print(numero, end=" x ")
    if calc in "SS":
        print(1, end=" = ")
    return print(multiply)


print('__'*35)
a = int(input(' Deseja calcular o fatorial de qual número?\n  R: '))

print('__'*35)
b = str(input(' Queres ver o cálculo feito?[Ss/Nn]\n  R: ')).upper()
while b not in "SSNN":
    b = str(input(' Queres ver o cálculo feito?[Ss/Nn]\n  R: ')).upper()

fatorial(a, b)
