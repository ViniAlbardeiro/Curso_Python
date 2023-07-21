from datetime import datetime

n = []

data_atual = (str(datetime.today()))
ano_atual = int(data_atual[0:4])

print('')

for i in range(0,7):
    ano_nascimento = int(input(' Digite o seu ano de nascimento: '))
    print(f'Idade A Completar -> {ano_atual - ano_nascimento} anos')
    if ano_atual - ano_nascimento >= 18:
        n.append(i)

if len(n) == 1:
    print(f'\n Apenas {(len(n))} pessoa é maior de idade, e {7 - (len(n))} são menores.')
elif 2 <= len(n) <= 5:
    print(f'\n {(len(n))} pessoas são maiores de idade e {7 - (len(n))} são menores.')
elif len(n) == 6:
    print(f'\n {len(n)} pessoas são maiores de idade e apenas {7 - len(n)} é menor.')
elif len(n) == 0:
    print('\n Todas as pessoas ainda são menores de idade.')
elif len(n) == 7:
    print('\n Todas as pessoas são maiores de idade.')