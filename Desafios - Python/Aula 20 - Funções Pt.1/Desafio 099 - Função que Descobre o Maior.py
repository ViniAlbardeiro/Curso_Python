from time import sleep
print('-='*30)


def maior(*nums):
    print(' Analisando os valores passados...')
    sleep(1)
    print(f' Os números são : ', end=' ')
    for num in nums:
        print(num, end='...')
        sleep(0.6)
    print()
    print(f' Foram digitados {len(nums)} valores.')
    sleep(0.7)
    print(f' O maior valor é {max(nums)}.')
    sleep(0.7)
    print('-='*30)


maior(5, 6, 4, 9, 10, 0)
maior(2, 4, 29)
maior(0)
