numero_1 = float(input('\n\033[33m Digite qualquer valor: '))
numero_2 = float(input('\033[33m Digite um outro valor qualquer: '))
opcoes_menu = int(input('\n\033[36m O que deseja fazer?'
                        '\n\033[31m     [0] Encerrar programa.'
                        '\n     [1] Continuar.'
                        '\n\033[36m Sua escolha: '))
print('\033[37m----------------------------------------------')

while opcoes_menu != 0:
    opcoes_menu = int(input('\n\033[36m O que quer fazer?'
    '\n\033[31m     [ 0 ] Encerrar o programa.'
    '\n     [ 1 ] Somar.'
    '\n     [ 2 ] Subtrair.'
    '\n     [ 3 ] Multiplicar.'
    '\n     [ 4 ] Dividir.'
    '\n     [ 5 ] Mudar valores.'
    '\n\033[36m Sua escolha: '))
    if opcoes_menu == 1:
        print('\n\033[35mVocê escolheu a função SOMA.')
        print(f'\n\033[35m A soma entre {numero_1} e {numero_2}, resulta em {numero_1 + numero_2}.')
        print('\033[37m----------------------------------------------')
    elif opcoes_menu == 2:
        print('\n\033[35mVocê escolheu a função SUBTRAÇÃO.')
        print(f'\n\033[35m A diferença entre {numero_1} e {numero_2}, resulta em {numero_1 - numero_2}.')
        print('\033[37m----------------------------------------------')
    elif opcoes_menu == 3:
        print('\n\033[35mVocê escolheu a função MULTIPLICAÇÃO.')
        print(f'\n\033[35m O produto entre {numero_1} e {numero_2}, resulta em {numero_1 * numero_2}.')
        print('\033[37m----------------------------------------------')
    elif opcoes_menu == 4:
        print('\n\033[35mVocê escolheu função DIVISÃO.')
        print(f'\n\033[35m A divisão entre {numero_1} e {numero_2}, resulta em {(numero_1 / numero_2):.2f}')
        print('\033[37m----------------------------------------------')
    elif opcoes_menu == 5:
        numero_1 = float(input('\n\033[33m Digite o primeiro valor: '))
        numero_2 = float(input('\033[33m Digite o segundo valor: '))
        print('\033[37m----------------------------------------------')

print('\n\033[37m Programa encerrado com sucesso! Pressione SHIFT + F10 para reiniciar o programa.')
print('\n\033[37m----------------------------------------------')