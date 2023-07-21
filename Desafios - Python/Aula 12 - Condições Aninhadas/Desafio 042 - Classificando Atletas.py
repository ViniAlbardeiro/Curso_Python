idade = int(input('\n Qual sua idade? '))

if idade > 9:
    print('Você pertence à classe Mirim.')
elif 9 <= idade < 14:
    print('Você pertece à classe Infantil.')
elif 14 <= idade < 19:
    print('Você pertence à classe Júnior.')
elif idade == 19:
    print('Você pertence à classe Sênior.')
elif idade >= 20:
    print('Você joga na classe Master.')