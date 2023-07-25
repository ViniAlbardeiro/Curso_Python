nums = []
switch = '0'

while switch not in 'Nn':
    n = int(input("\n Digite um número: "))
    nums.append(n)
    switch = '0'
    while switch not in 'SsNn':
        switch = str(input(" Deseja continuar? [S/N] "))

print('\n', '-'*30)
print(f'\n a)Foram digitados {len(nums)} números.')
nums.sort(reverse=True)
print(f'\n b)Os números em ordem decrescente fica: {nums}')
if 5 in nums:
    print('\n c)O cinco faz parte da lista.')
else:
    print('\n c)O cinco não faz parte da lista.')
