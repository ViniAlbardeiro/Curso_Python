

def dinheiro(num):
    while num.isalpha() == True or num in " ":
        print(' ERRO! DIGITE APENAS VALORES VÁLIDOS!')
        num = input(' Digite novamente: ')

    if "," in num:
        num = num.replace(',', '.')
    num = float(num)
    return num


