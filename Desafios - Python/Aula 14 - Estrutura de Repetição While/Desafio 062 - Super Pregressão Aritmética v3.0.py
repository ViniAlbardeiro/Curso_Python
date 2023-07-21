print('-' * 17)
print(' Gerador de PA')
print('-' * 17)

first = int(input('\n Primeiro Termo: '))
calcPA = int(input(' Razão Da Progressão: '))
addPos = 1
atualPos = []

print()
while addPos <= 10:
    print(f'\033[36m{first + (addPos - 1) * calcPA}', end=' -> ')
    addPos += 1
print('PAUSA')

mostPos = int(input('\n\033[m   Mais quantos termos devo mostrar: '))

while mostPos != 0:
    addPos = 1
    while addPos <= mostPos:
        print(f'\033[36m{(first + (addPos + sum(atualPos) + 9 ) * calcPA)}', end=' -> ')
        addPos += 1
    atualPos.append(mostPos)
    print('PAUSA')
    mostPos = int(input('\n\033[m   Mais quantos termos devo mostrar: '))

print('\033[31m Programa Encerrado')
