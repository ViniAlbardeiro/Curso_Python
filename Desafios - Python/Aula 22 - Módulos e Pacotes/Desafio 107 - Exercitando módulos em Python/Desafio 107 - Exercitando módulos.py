from moeda107 import (dobro, metade, aumento, reducao)

num = float(input(' Digite um valor: '))

print(f' O dobro de {num} é {dobro(num)}')
print(f' A metade de {num} é {metade(num)}')
print(f' O número {num} aumentado em 30% é igual a {aumento(num, 30)}')
print(f' O número {num} reduzido em 15% é igual a {reducao(num, 15)}')
