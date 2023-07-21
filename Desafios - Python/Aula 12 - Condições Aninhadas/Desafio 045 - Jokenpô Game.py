from random import choice

#cores
roxo = '\033[35m'
ciano = '\033[36m'
vermelho = '\033[31m'

#jogadores
jog = str(input(roxo + '\n  Suas opções de jogada.'
                   '\n   ->   Pedra.'
                   '\n   ->   Papel.'
                   '\n   ->   Tesoura.'
                   '\n Qual a sua jogada? '))
cpu = choice(['Pedra','Papel', 'Tesoura'])
jogada = jog.capitalize()

print(f'\n Jogador lançou {vermelho + jogada.upper()}')
print(f'{roxo} Cpu lançou {vermelho + cpu.upper()}')

print(ciano)
if jogada == cpu:
    print('EMPATE!!!')

elif jogada == 'Pedra' and cpu == 'Papel' or jogada == 'Papel' and cpu == 'Tesoura' or jogada == 'Tesoura' and cpu == 'Pedra':
    print('JOGADOR PERDEU!!!')

elif jogada == 'Pedra' and cpu == 'Tesoura' or jogada == 'Papel' and cpu == 'Pedra' or jogada == 'Tesoura' and cpu == 'Papel':
    print('JOGADOR GANHOU!!!')
