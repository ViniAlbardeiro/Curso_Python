

def ficha(nome_jogador, qt_gols):
    msg_gols = f'{qt_gols} gols.'
    if nome_jogador == "":
        nome_jogador = "<desconhecido>"
    if qt_gols == "":
        msg_gols = 'nenhum gol.'
    return print(f' O jogador {nome_jogador} fez {msg_gols}')


ficha(nome_jogador=input(' Qual o nome do jogador?\n R: '), qt_gols=input(f' Quantos gols foram feitos?\n R: '))
