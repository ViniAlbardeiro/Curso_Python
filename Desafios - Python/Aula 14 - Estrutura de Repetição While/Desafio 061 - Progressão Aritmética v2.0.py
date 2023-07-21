print('\n   -----------------------'
      '\n    Progressão Aritmética'
      '\n   -----------------------')

firstTerm = int(input('\n Primeiro Termo da Progressão: '))
reasonPA = int(input(' A Razão da Progressão: '))
c = 1

while (c != 11):
      print(f'{(firstTerm + (c - 1) * reasonPA)}', end=' -> ')
      c += 1
print('FIM')
