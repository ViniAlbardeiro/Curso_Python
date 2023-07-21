
listNumbers = []
print('\n   Ao digitar 999, o programa será encerrado!')
numberInput = 0

while numberInput != 999:
    numberInput = int(input('\n Digite um número qualquer: '))
    listNumbers.append(numberInput)
listNumbers.remove(999)
print(f'\n  Excetuando 999, foram digitados {len(listNumbers)} números, e a soma entre eles é {sum(listNumbers)}.')