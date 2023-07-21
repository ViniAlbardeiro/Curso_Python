from random import randint
from time import sleep

print('\n CPU sorteando um número entre 0 e 10...')
sleep(5)
jogada_cpu = randint(0, 10)
print(' Pronto, número escolhido!')
jogada_player = int(input(' Agora, tente adivinhar o número escolhido pela CPU: '))
n_jogadas = []

while jogada_player != jogada_cpu:
    jogada_player = int(input('\n Tente adivinhar novamente: '))
    n_jogadas.append(jogada_player)

print(f'\n Parabéns, você acertou! Foram necessários {len(n_jogadas)+1} palpites para ganhar!')
