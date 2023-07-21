num = add = 0
cont = 0

while True:
    num = int(input('Digite um número(999 para encerrar):'))
    if num == 999:
        break
    add += num
    cont += 1
print(f'\n A soma dos {cont} valores, é {add}')
