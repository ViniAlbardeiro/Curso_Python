
kmp = float(input('\n Digite o valor do Km rodado: '))
dp = float(input(' Digite o valor do dia do carro: '))
d = int(input(' Digite a quantidade de dias que o carro foi usado: '))
km = float(input(' Digite quantos Km foram rodados: '))

print(f'\n O custo dos dias em que o carro foi usado é de R${dp * d:.2f}'
      f' e o custo dos Km rodados é de R${kmp * km:.2f},'
      f' totalizando R${(kmp * km)+(dp * d):.2f}')
