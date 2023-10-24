

def leia_int(n):
    while n not in '0123456789' or n in\
            "":
        print(f'\033[:31m ERRO! DIGITE UM VALOR VÁLIDO! \033[m')
        n = input(' Digite um número novamente: ')
    return n

n = leia_int(input(' Digite um número: '))
print("__"*30)
print(f' Você digitou o número {n}')
