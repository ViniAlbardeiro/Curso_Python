verde = '\033[32m'

day = input(verde + '\n Insira o dia do seu nascimento: ')
month = input (' Insira o mês do seu nascimento: ')
year = input (' Insira o ano do seu nascimento: ')

print(f"\n Você nasceu em \033[4;33m{day} de {month} de {year}\033[0;32m. Correto?\033[m")