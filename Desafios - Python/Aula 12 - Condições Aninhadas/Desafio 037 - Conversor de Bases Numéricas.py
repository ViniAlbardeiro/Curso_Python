# Entrada do valor a ser convertido.
num = int(input('\n\033[31m Digite um número: '))

# Base para a conversão.
con = int(input('\n Agora, escolha uma das bases de conversão:'
      '\n\033[36m[1] --> Binário.'
      '\n[2] --> Octal.'
      '\n[3] --> Hexadecimal.'
      '\n\033[31m Sua opção: '))


if con == 1:
    print(f'\033[35m{num}\033[36m convertido na base binária, é \033[35m{bin(num)}.')

elif con == 2:
    print(f'\033[35m{num}\033[36m convertido na base octal, é \033[35m{oct(num)}.')

elif con == 3:
    print(f'\033[35m{num}\033[36m convertido na base hexadecimal, é \033[35m{hex(num)}.')
