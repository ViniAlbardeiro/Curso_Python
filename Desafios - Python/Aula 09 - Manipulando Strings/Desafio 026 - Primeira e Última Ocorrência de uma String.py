frase = str(input('\n Digite uma frase: ')).strip().upper()



print('\n A letra A apareceu ',frase.count('A'),'vezes.')
print(' A primeira letra A apareceu na posição', (frase.find('A')) +1,'.')
print(' A última letra A apareceu na posição', frase.rfind('A') +1, '.')

