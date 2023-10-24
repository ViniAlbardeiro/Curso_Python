

def voto(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento
    if idade < 18:
        return print(f"Com {idade} anos, o voto NÃO É PERMITIDO.")
    elif 18 <= idade < 65:
        return print(f' Com {idade} anos, o voto é OBRIGATÓRIO.')
    else:
        return print(f' Com {idade} anos, o voto é OPCIONAL.')


voto(int(input(' Digite a data de seu nascimento: ')))
