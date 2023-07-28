nums = [[], []]

for q in range(0, 7):
    num = int(input('\n Digite um número: '))
    if num % 2 == 0:
        nums[0].append(num)
        nums[0].sort()
    else:
        nums[1].append(num)
        nums[1].sort()
print()
print('-'*25)
print(f'\n Os números pares digitados são -> {nums[0]}.')
print(f' Os números ímpares digitados são -> {nums[1]}.')
