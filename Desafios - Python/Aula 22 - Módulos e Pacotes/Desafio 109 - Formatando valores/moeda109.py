

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
    num += num*taxa/100
    if money is True:
        formatnum = "R$" + str(num).replace(".0", ",00")
        return formatnum
    else:
        return num


def reducao(num, taxa, money):
    num -= num*taxa/100
    if money is True:
        formatnum = "R$" + str(num).replace(".0", ",00")
        return formatnum
    else:
        return num


def moeda(num):
    moedaformat = 'R$' + str(num) + '0'
    return moedaformat
