nums = []
odd = []
pair = []

while True:
    n = int(input('\n Digite um valor: '))
    nums.append(n)
    if n % 2 == 0:
        pair.append(n)
    else:
        odd.append(n)
    switch = str(input(' Deseja continuar? [S/N] '))
    while switch not in "SsNn":
        switch = str(input(' Deseja continuar? [S/N] '))
    if switch in "Nn":
        break

print(
    f'\n Os números digitados foram: {nums}.'
    f'\n Os números pares digitados são: {pair}.'
    f'\n Os números ímpares digitados são: {odd}.'
)