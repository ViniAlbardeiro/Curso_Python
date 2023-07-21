salario = float(input('\n Digite o salário do funcionário: '))

if salario >= 1250:
    print(f'O salário desse funcionário passa a ser de {salario * 1.10}')
else:
    print(f'O salário desse funcionário passa a ser de {salario * 1.15 }')
