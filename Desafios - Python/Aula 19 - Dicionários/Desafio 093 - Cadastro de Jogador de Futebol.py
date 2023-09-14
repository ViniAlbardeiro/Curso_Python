jogador = dict()
gols = list()

jogador["nome"] = str(input('\n Nome do Jogador: '))
jogador["partidas"] = int(input(f' Partidas jogadas por {jogador["nome"]}: '))
for jogo in range(0, jogador["partidas"]):
    gols.append(int(input(f' Gols feitos na partida {jogo}: ')))
    jogador["gols"] = gols
jogador["total"] = sum(gols)

# print(gols)
# print(jogador)

print(f'\n O jogador {jogador["nome"]} jogou {jogador["partidas"]} jogos.')
for count in range(0, jogador["partidas"]):
    print(f'     -> Na partida {count}, fez {jogador["gols"][count]} gols.')
print(f' Fez um total de {jogador["total"]} gols.')