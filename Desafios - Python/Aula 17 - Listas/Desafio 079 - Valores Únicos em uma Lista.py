numList = []

while True:
    n = int(input('\n Digite um número: '))
    if n not in numList:
        print(' Valor adicionado com sucesso!')
        numList.append(n)
    else:
        while n in numList:
            n = int(input(' Valor já digitado, escreva outro...: '))
        numList.append(n)
    switch = str(input(' Quer continuar? [S/N] '))
    if switch in 'Nn':
        break

numList.sort()
print(f'\n Os números digitados são: ', end= ' ')

for num in numList:
    print(num, end= '...')
