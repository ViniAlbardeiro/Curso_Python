numList = []
numInput = 0
condition = 's'

while condition in ['S', 's']:
    numInput = int(input('\n Digite um número qualquer: '))
    condition = input('Deseja continuar?[S/N]: ')
    numList.append(numInput)

numList.sort()
print(f'\n A média dos valores digitados é {((sum(numList)) / len(numList)):.2f}')
print(f' O menor valor é {numList[0]} e o maior valor é {numList[-1]}.')
