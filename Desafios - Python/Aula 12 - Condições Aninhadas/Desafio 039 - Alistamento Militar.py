from datetime import date

ano = int(input('\n\033[31m Ano de nascimento: '))
data = str(date.today()) #date.today(year-month-day)
idade = int(data[0:4]) - ano

print(f'Quem nasceu em \033[36m{ano}\033[31m, faz \033[36m{idade} anos\033[31m em \033[36m{data[0:4]}.')

if idade > 18:
    print('\n\033[36m Se você não se alistou, deveria ter feito antes!')
elif idade == 18:
    print('\n\033[36m Você se alistar em alguma força esse ano.')
elif idade < 18:
    print(f'\n\033[36m Faltam apenas {18 - idade} ano(s) para você se alistar.')
