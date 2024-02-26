from moedas108 import (dobro, metade, aumento, reducao, moeda)

num = float(input(' Digite um valor: '))

print(f' O dobro de {moeda(num)} é igual a {moeda(dobro(num))}')
print(f' A metade de {moeda(num)} é igual a {moeda(metade(num))}')
print(f' Um valor de {moeda(num)} com 30% de aumento equivale a {moeda(aumento(num, 30))}')
print(f' Um valor de {moeda(num)} reduzido em 15% equivale a {moeda(reducao(num, 15))}')
