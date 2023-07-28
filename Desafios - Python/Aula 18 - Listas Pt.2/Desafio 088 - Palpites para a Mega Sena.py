from random import randint
from time import sleep
palpites = []
jogadas = []

numPalpites = int(input(' Quantos números deseja sortear? '))

for cont in range(1, numPalpites + 1):

    c = 0
    while c != 6:
        n = randint(0, 60)
        jogadas.append(n)
        c += 1

    palpites.append(jogadas[:])
    jogadas.clear()

print(f'Sorteando {numPalpites} Jogos'.center(40, '-'))
sleep(2)
for jogada in palpites:
    print(f' Jogo {palpites.index(jogada) + 1}: {jogada}')
    sleep(1)
