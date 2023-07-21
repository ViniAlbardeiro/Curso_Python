from random import randint
from time import sleep as sl

# teste
# teste
numgames = 0
result = 0
while True:
    print('--'*20)
    player = int(input('Digite um valor: '))
    jogada = input('Par ou Ímpar? [P/I]: ')
    print('--'*20)
    cpu = randint(0, 11)
    placar = (player+cpu)%2
    if (player + cpu)% 2 == 0:
        result = ['p', 'P']
        print(f'O jogador escolheu {player}, e a cpu escolheu {cpu}. O total de {player + cpu} é PAR.')
        print('=-=' * 20)
        if jogada in result:
            numgames += 1
            print('Você venceu!')
            print('Vamos jogar novamente...')
            sl(2)
        else:
            print('Você perdeu. =(')
            break
    else:
        result = ['i', 'I']
        print(f'O jogador escolheu {player}, e a cpu escolheu {cpu}. O total de {player+cpu} é ÍMPAR')
        print('=-=' * 20)
        if jogada in result:
            numgames += 1
            print('Você venceu!')
            print('Vamos jogar novamente...')
            sl(2)
        else:
            print('Você perdeu. =(')
            break

print(f'GAME OVER, você venceu {numgames} vezes.')