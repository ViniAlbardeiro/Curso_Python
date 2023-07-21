
while True:
    print("-" * 40)
    num = int(input("Quer ver a tabuada de qual número? \n R: "))
    print("-" * 40)
    if num < 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
print("-" * 40)
print('Fim')