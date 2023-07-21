n = int(input('\n Digite um número: '))

print(f'Unidade de Milhar: {n // 1000 % 10}')
print(f'Centena: {n // 100 % 10}')
print(f'Dezena: {n // 10 % 10}')
print(f'Unidade: {n // 1 % 10}')

# Não consegui resolver
