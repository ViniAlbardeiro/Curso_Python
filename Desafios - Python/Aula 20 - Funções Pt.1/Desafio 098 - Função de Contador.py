from time import sleep


def contador(i, f, p):
    if i < f:
        if p < 0:
            p = p*-1
        if p == 0:
            p = 1
        for nums in range(i, f+1, p):
            print(nums, end=' ')
            sleep(0.75)
        print('Fim')
    elif i > f:
        if p == 0:
            p = 1
        if p < 0:
            p = p*-1
        for nums in range(i, f - 1, -p):
            print(nums, end=' ')
            sleep(0.75)
        print('Fim')


# Questão A
print('_'*40)
print('Contagem de 1 a 10 de 1 em 1')
contador(1, 10, 1)
# Questão B
print('_'*40)
print('Contagem de 10 a 0 de 2 em 2')
contador(10, 0, 2)
# Questão C
while True:
    print('_'*40)
    print(' Contagem Personalizada')
    contador(
        i=int(input(' Início: ')),
        f=int(input(' Fim: ')),
        p=int(input(' Passo: '))
    )
    print()
    print('_' * 40)
    while True:
        interruptor = input(' Queres continuar? [S/N]: ').upper()
        if interruptor in "SN":
            break
    if interruptor in "N":
        break
print('_'*40)
print('FIM')
