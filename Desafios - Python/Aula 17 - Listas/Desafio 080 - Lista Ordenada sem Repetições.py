numList = []

for c in range(0, 5):
    num = int(input(' Digite um número: '))

    if len(numList) == 2:
        if num < min(numList):
            c = 0
            numList.insert(0, num)
        elif num > max(numList):
            c = len(numList)
            numList.append(num)
        else:
            numList.insert()


    if len(numList) in (1, 2):
        print(max(numList), min(numList))
        if num < min(numList):
            c = 0
            numList.insert(0, num)
        else:
            numList.append(num)

    if len(numList) == 0:
        numList.append(num)

    print(f' O valor foi adicionado na posição {c+1}')
    print(numList)

