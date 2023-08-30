from random import randint
from time import sleep

jogadores = dict()
jogadores['Jogador1'] = randint(1, 6)
jogadores['Jogador2'] = randint(1, 6)
jogadores['Jogador3'] = randint(1, 6)
jogadores['Jogador4'] = randint(1, 6)
orderedPlays = sorted(jogadores.values(), reverse=True)
rankingPlayers = list()

print('\n                 Valores Sorteados: \n')
for jogada in jogadores.keys():
    print(f'     O {jogada} sorteou {jogadores[jogada]}')
    sleep(2)
print('\n                 Ranking Dos Jogadores\n')

for n in range(0, len(jogadores)):
    for player, points in jogadores.items():
        if orderedPlays[n] == points:
            if player not in rankingPlayers:
                rankingPlayers.append(player)

for pos, joga in enumerate(rankingPlayers):
    print(f'     {pos + 1}º -> {joga} -> {jogadores[joga]}pts.')
    sleep(2)
