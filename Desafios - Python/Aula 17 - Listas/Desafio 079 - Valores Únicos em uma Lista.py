numList = []

while True:
    n = int(input(' Digite um número: '))
    if n in numList:
        print(' Valor já digitado. Digite outro...')
    else:
        print(' Valor adicionado com sucesso...')
        numList.append(n)

    switch = str(input(' Quer continuar? [S/N] '))
    if switch in 'Nn':
        break

numList.sort()
print(f'\n Os números digitados são: ', end= ' ')

for num in numList:
    print(num, end= '...')
