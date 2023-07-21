print('\n\033[34m==============================')
print('    Detector de Palíndromo')
print('==============================')

fr = input('\n\033[31m Digite uma frase: ').lower()
frl = (''.join(fr.split()))

for i in range(1, (len(frl)+1)//2):
    if frl[-1+i] == frl[0-i]:
        v = 0
    else:
        v = 1

if v == 0:
    print('\n\033[35m  Essa frase é um palíndromo!')
else:
    print('\n\033[35m  Essa frase não é um palíndromo!')