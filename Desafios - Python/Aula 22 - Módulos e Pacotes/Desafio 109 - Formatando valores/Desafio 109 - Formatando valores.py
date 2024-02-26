from moeda109 import (dobro, metade, aumento, reducao, moeda)

num = float(input(' Digite um valor:'))
print(f'O valor analisado é {moeda(num)}')
print(f' Seu dobro vale {dobro(num, True)}')
print(f' Sua metade vale {metade(num, True)}')
print(f' Seu valor com um aumento de 40% vale {aumento(num, 40, True)}')
print(f' Seu valor com uma redução de 15% vale {reducao(num, 15, True)}')
