from statistics import mean
listaControle = list()
pessoas = list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa["nome"] = str(input(' Nome: ')).capitalize().strip()
    while True:
        pessoa["sexo"] = str(input(' Sexo [M/F]: ')).upper()
        if pessoa["sexo"] in "MF":
            break
        print('ERRO! DIGITE (M) OU (F) PARA CONTINUAR')
    pessoa["idade"] = int(input(' Idade: '))
    pessoas.append(pessoa.copy())
    while True:
        resposta = str(input(' Quer continuar? [S/N]: ')).upper()
        if resposta in "SN":
            break
        print('ERRO! DIGITE (S) OU (N) PARA CONTINUAR.')
    if resposta in 'N':
        break
print('--'*20)

# Questão A. Quantidade de pessoas cadastradas
print(f' Há um total de {len(pessoas)} pessoas cadastradas.')

# Questão B. Média de idade do grupo
for idadePessoa in pessoas:
    listaControle.append(idadePessoa["idade"])
print(f' A média das idade é de {mean(listaControle)} anos.')

# Questão C. Lista com todas as mulheres.
print(f' As mulheres cadastradas foram:', end=" ")
for mulheres in pessoas:
    if 'F' in mulheres["sexo"]:
        print(f'{mulheres["nome"]}', end=" ")

# Questão D. Pessoas com idade acima da média.
print('As pessoas com idade acima da média são: ')
for cadastro in pessoas:
    if cadastro["idade"] > mean(listaControle):
        print(f' {cadastro["nome"]} com {cadastro["idade"]} anos.')
