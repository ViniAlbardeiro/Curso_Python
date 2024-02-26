# num = float(input(' Digite um valor:'))
# print(f'O valor analisado é {moeda(num)}')
# print(f' Seu dobro vale {dobro(num, True)}')
# print(f' Sua metade vale {metade(num, True)}')
# print(f' Seu valor com um aumento de 40% vale {aumento(num, 40, True)}')
# print(f' Seu valor com uma redução de 15% vale {reducao(num, 15, True)}')


def resumo(n, taxa_aum, taxa_red):
    def dobro(num, money):
        num *= 2
        if money is True:
            formatnum = "R$" + str(num).replace(".0", ",00")
            return formatnum
        else:
            return num

    def metade(num, money):
        num /= 2
        if money is True:
            formatnum = "R$" + str(num).replace(".0", ",00")
            return formatnum
        else:
            return num

    def aumento(num, taxa, money):
        num += num * taxa / 100
        if money is True:
            formatnum = "R$" + str(num).replace(".0", ",00")
            return formatnum
        else:
            return num

    def reducao(num, taxa, money):
        num -= num * taxa / 100
        if money is True:
            formatnum = "R$" + str(num).replace(".0", ",00")
            return formatnum
        else:
            return num

    def moeda(num):
        moedaformat = 'R$' + str(num) + '0'
        return moedaformat

    valor = moeda(n)
    dobro = dobro(n, True)
    metade = metade(n, True)
    aumento = aumento(n, taxa_aum, True)
    reducao = reducao(n, taxa_red, True)

    return print("", '-' * 40 + '\n',
                 'RESUMO'.center(40)+'\n',
                 '-' * 40,
                 f"\n Valor Analisado: {n}",
                 f'\n Seu dobro: {dobro}',
                 f'\n Sua metade: {metade}',
                 f'\n Com um aumento de {taxa_aum}%: {aumento}',
                 f'\n Com uma reduçao de {taxa_red}%: {reducao}')
