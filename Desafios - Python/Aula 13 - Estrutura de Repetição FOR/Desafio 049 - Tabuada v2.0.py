t = int(input('\nQual tabuada você quer?'
              '\n Sua escolha: '))
f = int(input('\nAté que número termina sua tabuada?'
              '\n Sua escolha: '))

print(f'\n    Tabuada do {t}')

for i in range(1, f+1):
    print(f'{t} * {i} = {t*i}')