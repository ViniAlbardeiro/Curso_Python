expList = []

exp = input('\n Digite uma expressão qualquer: ')
for digit in exp:
    expList.append(digit)

if expList.count('(') == expList.count(')'):
    print(' Essa expressão é válida.')
else:
    print(' Essa expressão não é válida.')
