print('-' * 30)
print('    Sequência de Fibonacci')
print('-' * 30)

totalSeq = int(input('\n Quantos termos devo mostrar: '))
seqFibo = [0, 1]

while len(seqFibo) <= totalSeq + 1:
    print(f'  {seqFibo[(len(seqFibo) - 2)]}', end=' ->')
    seqFibo.append(seqFibo[-1] + seqFibo[-2])
print('  FIM')
