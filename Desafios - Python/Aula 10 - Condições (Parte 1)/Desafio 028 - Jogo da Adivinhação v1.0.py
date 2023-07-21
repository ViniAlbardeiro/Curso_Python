from random import randint

print('\n\033[0;36m Seja bem-vindo ao Jogo da Adivinhação 1.0!')
print('\n Modo de Jogar:\n   O computador vai selecionar um número entre 0 e 5'
      ' e você terá que adivinhá-lo. Se acertar você ganha, senão, perde.\033[m')

cpu = int(randint(0, 5))
player = int(input('\n \033[0;33m Digite um número entre 0 e 5: \033[m'))

if player == cpu:
    print(f'          A máquina escolheu {cpu}. Parabéns, você acertou!')
else:
    print(f'          A máquina escolheu {cpu}. Que pena, você errou!')
