moneyNote50 = moneyNote20 = moneyNote10 = moneyNote01 = 0

print("="*26)
print('  Bem vindo ao Banco H&A')
print("="*26)

money = int(input('\n Digite o valor a ser sacado: '))
print('')
while True:
    if money >= 50:
        while money >= 50:
            money -= 50
            moneyNote50 += 1
    elif money >= 20:
        while money >= 20:
            money -= 20
            moneyNote20 += 1
    elif money >= 10:
        while money >= 10:
            money -= 10
            moneyNote10 += 1
    elif money >= 1:
        money -= 1
        moneyNote01 += 1
    else:
        break
phrase50 = f'   {moneyNote50} cédulas de 50 reais.'
phrase20 = f'   {moneyNote20} cédulas de 20 reais.'
phrase10 = f'   {moneyNote10} cédula de 10 reais.'
phrase01 = f'   {moneyNote01} cédulas de 1 real.\n'
print('*'*30)
print('\n Você deve receber:')
if moneyNote50 == 0:
    phrase50 = ''.strip()
if moneyNote20 == 0:
    phrase20 = ''.strip()
if moneyNote10 == 0:
    phrase10 = ''.strip()
if moneyNote01 == 0:
    phrase01 = ''.strip()
print(phrase50)
print(phrase20)
print(phrase10)
print(phrase01)
print('*'*30)
print('\n Felizes em ajudar! Volte sempre!')