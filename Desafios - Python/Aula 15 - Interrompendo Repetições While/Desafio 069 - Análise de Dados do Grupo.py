# ler idade
# ler sexo
# repetir infinitamente até que o usuario deseje encerrar
# não aceitar dados diferentes do que foi pedido.
# tratar os dados recebidos

dataQuestion1 = []
dataQuestion2 = []
dataQuestion3 = []

while True:
    ageGroup = int(input('\n Idade: '))
    sexGroup = str(input(' Sexo: '))
    while sexGroup not in ["M", 'm', 'F', 'f']:
        sexGroup = str(input(' Sexo: '))
    offOn = str(input('\n Deseja continuar? [S/N] -> '))
    while offOn not in ['s', 'S', 'n', 'N']:
        offOn = str(input('\n Deseja continuar? [S/N] -> '))
    if ageGroup >= 18:
        dataQuestion1.append(ageGroup)
    if sexGroup in ['m', 'M']:
        dataQuestion2.append(sexGroup)
    if sexGroup in ['f', 'F'] and ageGroup < 20:
        dataQuestion3.append([ageGroup, sexGroup])
    if offOn in ['n', 'N']:
        break


# Quantas pessoas tem mais de 18 anos de idade
print(f'\n {len(dataQuestion1)} pessoas tem mais de 18 anos de idade.')

# Quantos homens foram cadastrados.
print(f'\n {len(dataQuestion2)} pessoas são homens.')

# Quantas mulheres tem menos de 20 anos de idade
print(f'\n {len(dataQuestion3)} mulheres têm menos de 20 anos de idade.')
