

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
        num -= (num * taxa / 100)
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
    ljustvar = 40
    rjustvar = 10

    return print("", '-' * 40 + '\n',
                 'RESUMO'.center(40)+'\n',
                 '-' * 40,
                 "\nValor Analisado".ljust(ljustvar) + f"{valor}",
                 '\nSeu dobro'.ljust(ljustvar) + f'{dobro}',
                 '\nSua metade'.ljust(ljustvar) + f'{metade}',
                 f'\nAumento de {taxa_aum}%'.ljust(ljustvar) + f'{aumento}',
                 f'\nRedução de {taxa_red}%'.ljust(ljustvar) + f'{reducao}')
