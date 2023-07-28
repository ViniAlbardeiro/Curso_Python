nums = []
pair = []
a = b = 0

while a != 3:
    num = int(input(f' Digite um valor para a posição [{a}, {b}]: '))
    nums.append([num])
    b += 1
    if b == 3:
        a += 1
        b = 0
print()
print('-+-' * 15)
print()

for i in nums:
    print(' ', i, end='  ')
    if i in (nums[2], nums[5], nums[8]):
        print()

for c in nums:
    for n in c:
        if n % 2 == 0:
            pair.append(n)

print(f' A soma dos números pares digitados é: {sum(pair)}')
print(f' Os números da 3ª coluna somam: {nums[2] + nums[5] + nums[8]}')
print(f' O maior valor da 2ª coluna é {max(nums[3], nums[4], nums[5])}')
