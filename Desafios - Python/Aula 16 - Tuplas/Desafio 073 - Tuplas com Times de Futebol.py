teams = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético - MG',
         'Botafogo', 'Athletico - PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético - GO')

print(f'\n Todos os times do Brasileirão: {teams}.\n')
print('-='*24)
print(f'\n Os cinco primeiros colocados são: {teams[:5]}.\n')
print('-='*24)
print(f'\n Os quatro últimos colocados são: {teams[-4:]}.\n')
print('-='*24)
print(f'\n Em ordem alfabética, os times ficam na ordem {sorted(teams)}.\n')
print('-='*24)
print(f'\n O time Chapecoense, de acordo com a tabela, está na posição {teams.index("Chapecoense") + 1}.\n')
