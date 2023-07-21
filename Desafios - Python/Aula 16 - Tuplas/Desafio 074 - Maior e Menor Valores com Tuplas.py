from random import randint

num0 = randint(0, 25)
num1 = randint(0, 25)
num2 = randint(0, 25)
num3 = randint(0, 25)
num4 = randint(0, 25)

tupleNums = (num0, num1, num2, num3, num4)
listNums = sorted(tupleNums)

print(f'\n Os números aleatórios gerados são: {tupleNums}')
print(f'\n Os números gerados ordenados ficam: {listNums}')
print(f'\n O maior número gerado foi: {listNums[-1]}')
print(f'\n O menor número gerado foi: {listNums[0]}')
