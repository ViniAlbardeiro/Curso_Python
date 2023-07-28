nums = []
a = b = 0

while a != 3:
    num = int(input(f' Digite um valor para a posição [{a}, {b}]: '))
    nums.append([num])
    b += 1
    if b == 3:
        a += 1
        b = 0

print('-+-' * 15)

for i in nums:
    print(' ', i, end='  ')
    if i in (nums[2], nums[5]):
        print()
