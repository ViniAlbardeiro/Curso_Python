
p = float(input('\n Digite o preço do produto: '))
d = float(input(' Digite o valor do desconto: '))

print(f'\n O produto com desconto custará R${(1-(d/100))*p:.2f}')
