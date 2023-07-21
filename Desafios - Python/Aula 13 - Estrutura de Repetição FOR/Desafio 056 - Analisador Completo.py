
idade_media = []
dados_masc = []
dados_fem = []

print('-----------------------------------------')
for p in range(1, 5):
    print(f"Dados da {p}ª pessoa\n")
    nome = input(' Nome:> ')
    idade = int(input(' Idade:> '))
    sexo = input(' Sexo [M/F]:> ')
    print('-----------------------------------------')
    idade_media.append(idade)
    if sexo == 'm' or sexo == 'M':
        dados_masc.append([idade, nome])
    if sexo == 'f' and idade < 20 or sexo == 'F' and idade < 20:
        dados_fem.append([idade, nome])

print('===============================================\n')

dados_masc.sort()       # Aqui a lista que contém idade e nome dos homens, são ordenadas, do 'menor para o maior'
print(f' A média aritmética das idades é {sum(idade_media)/len(idade_media)}')

    # na linha abaixo, onde as listas foram chamadas, existem dois pares de colchetes, isso porque o primeiro chama
    # uma das duas listas dentro dela, e a segunda, escolhe o dado específico da lista chamada.
print(f'O mais velho dentre os homens tem {dados_masc[-1][0]} anos e se chama {dados_masc[-1][1]} ')

if len(dados_fem) == 0:
    print("Nenhuma mulher tem menos de 20 anos.")
elif len(dados_fem) == 1:
    print(f"{len(dados_fem)} mulher tem menos de 20 anos.")
else:
    print(f"{len(dados_fem)} mulheres têm menos de 20 anos.")
