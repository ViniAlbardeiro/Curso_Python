from cadastro_de_pessoas import (cadastro, escrever, leitura, menu)

menu()

while True:
    try:
        optionChoice = int(input(" Sua Opção: "))
    except (ValueError, NameError):
        print('\033[31m'+'ERRO! DIGITE UM VALOR INTEIRO VÁLIDO!'+'\033[m')
    else:
        if 3 < optionChoice or optionChoice < 1:
            print("\033[31mOPÇÃO NÃO ESPECIFICADA! ESCREVA UM NÚMERO COM UMA OPÇÃO VÁLIDA!\033[m")
        else:
            match optionChoice:
                case 1:
                    leitura()
                    menu()
                case 2:
                    nome = input(' Nome: ')
                    idade = input(' Idade: ')
                    print('\033[32m CADASTRO REALIZADO COM SUCESSO!\033[m')
                    escrever(cadastro(nome, idade))
                    menu()
                case 3:
                    print('\033[32m OBRIGADO POR USAR NOSSO SISTEMA! VOLTE SEMPRE!\033[m')
                    break
