# Faça um programa que tenha uma função "notas()" que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações: Qt de notas
# a maior nota, a menor nota, a média da turma e a situação da turma.
from statistics import mean


def nota_alunos(*notas):
    analise_notas = dict()
    analise_notas["qt_notas"] = len(notas)
    analise_notas["maior_nota"] = max(notas)
    analise_notas["menor_nota"] = min(notas)
    analise_notas["media_notas"] = mean(notas)
    situacao_turma = ""
    if analise_notas["media_notas"] > 6:
        situacao_turma = "A turma foi APROVADA."
    elif analise_notas["media_notas"] <= 5:
        situacao_turma = "A turma está em RECUPERAÇÃO."
    else:
        situacao_turma = "A turma foi REPROVADA."
    analise_notas["situacao_turma"] = situacao_turma

    return analise_notas


print('\n', nota_alunos(5.5, 6, 7, 4))
