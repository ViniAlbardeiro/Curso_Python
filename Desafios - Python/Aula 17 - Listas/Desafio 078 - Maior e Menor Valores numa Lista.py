nums = []

print()
for cont in range(0,5):
    nums.append(int(input(' Digite um valor: ')))
print(f'\n O menor valor é {min(nums)} e está na {nums.index(min(nums)) + 1}º posição.')
print(f'\n O maior valor é {max(nums)} e está na {nums.index(max(nums)) + 1}º posição.')
