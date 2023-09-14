jogador = dict()
jogadores = list()
gols = list()

while True:
    print('-'*60)
    jogador.clear()
    gols.clear()
    jogador["nome"] = str(input('Nome do Jogador: ')).capitalize()
    jogador["numPartidas"] = int(input(f' Número de Jogos do {jogador["nome"]}: '))
    for partida in range(1, jogador["numPartidas"]+1):
        gols.append(int(input(f' Gols feitos na partida {partida}: ')))
    jogador["gol"] = gols.copy()
    jogadores.append(jogador.copy())
    resposta = str(input(' Quer continuar? [S/N]: ')).capitalize()
    while resposta not in "SN":
        print("ERRO, DIGITE APENAS [S] OU [N]!")
        resposta = str(input(' Quer continuar? [S/N]: ')).capitalize()
    if resposta == 'N':
        break
print('-='*30)

print('Cód.'.ljust(16, " "), 'Nome'.ljust(16, " "), 'Partidas'.ljust(20, " "), 'Gols'.ljust(20, " "), 'Total de Gols')
print("-"*100)

for codigo, player in enumerate(jogadores):
    print(str(codigo).ljust(20, " "), player["nome"].ljust(24, " "), str(player["numPartidas"]).ljust(19, " "), str(player["gol"]).ljust(30, " "), str(sum(player["gol"])))

while True:
    print('-=' * 30)
    chamadaJogador = int(input(' Para acessar os dados, digite o índice do jogador[999 para encerrar]: '))
    if chamadaJogador == 999:
        print('    Programa encerrado!')
        break
    elif chamadaJogador > len(jogadores):
        print(f'     Não há jogador cadastrado no índice {chamadaJogador}.')
    else:
        print(jogadores[chamadaJogador-1])
