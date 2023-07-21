num1 = int(input('\n Digite um valor qualquer: '))
num2 = int(input('\n Digite um outro valor: '))
num3 = int(input('\n Digite outro: '))
num4 = int(input('\n Digite o último: '))

tupleNums = (num1, num2, num3, num4)

print(f'\n O número 9 apareceu {tupleNums.count(9)} vezes.')
if 3 in tupleNums:
    print(f' O número 3 foi digitado na {tupleNums.index(3) + 1}º posição.')
else:
    print(' O número 3 não foi digitado.')

print(' Os números pares digitados são: ',end=' ')
for c in tupleNums:
    if c % 2 == 0:
        print(c, end=' ')
