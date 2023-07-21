list = []
switch = '0'

while switch not in 'Nn':
    n = int(input("\n Digite um número: "))
    list.append(n)
    switch = '0'
    while switch not in 'SsNn':
        switch = str(input(" Deseja continuar? [S/N] "))

print('\n', '-'*30)
print(f'\n a)Foram digitados {len(list)} números.')
print(f'\n b)Os números em ordem decrescente fica: {list.sort(reverse=True)}')
if 5 in list:
    print('\n c)O cinco faz parte da lista.')
else:
    print('\n c)O cinco não faz parte da lista.')
