a = int(input('\n\033[31m Primeiro valor: '))
b = int(input(' Segundo valor: '))

if a > b:
    print('\n\033[36m O primeiro valor é maior.')
elif a < b:
    print('\n\033[36m O segundo valor é maior.')
elif a == b:
    print('\n\033[36m Os dois valores são iguais.')