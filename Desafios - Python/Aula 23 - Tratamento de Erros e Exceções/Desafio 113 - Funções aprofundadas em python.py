while True:
    try:
        inteiro = int(input(' Digite um número inteiro: '))
    except (ValueError, NameError):
        print('\033[31m ERRO! O VALOR DIGITADO NÃO É VÁLIDO!\033[m')
    except KeyboardInterrupt:
        print('\n\n O usuário preferiu encerrar o programa.')
        break
    else:
        break

while True:
    try:
        real = float(input(' Digite um número real: '))
    except (ValueError, NameError):
        print('\033[31m ERRO! O VALOR DIGITADO NÃO É VÁLIDO!\033[m')
    except KeyboardInterrupt:
        print('\n\n O usuário preferiu encerrar o programa.')
        break
    else:
        break

print('-'*30)
print(f' Você digitou o número inteiro {inteiro} e o número real {real}')
