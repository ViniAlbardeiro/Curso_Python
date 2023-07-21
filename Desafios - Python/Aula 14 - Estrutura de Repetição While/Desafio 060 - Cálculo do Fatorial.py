from math import prod

print('\n---------------------'
      '\n Cálculo de fatorial'
      '\n---------------------')

num = int(input('\n Escreva um número: '))
calcFactList = []
nLoop = 1

while nLoop != num+1:
    calcFactList.append(nLoop)
    nLoop += 1

print(f'{num}! = {prod(calcFactList)}')






#numb = int(input('\n Escreva um número: '))
#calcFact = []

#for f in range(1, numb+1):
#    calcFact.append(f)

#print(f'{numb}! = {prod(calcFact)}')
