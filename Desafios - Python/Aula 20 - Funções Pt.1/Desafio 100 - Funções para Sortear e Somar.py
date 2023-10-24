from random import randint
from time import sleep
listaSorteio = list()
listaPares = list()


def sorteia():
    print(' Sorteando os números: ', end=' ')
    for contador in range(0, 5):
        num = randint(0, 100)
        print(num, end=' ')
        listaSorteio.append(randint(0, 100))


def soma_par():
    soma = 0
    for numero in listaSorteio:
        if numero % 2 == 0:
            soma = soma + numero
            listaPares.append(numero)
    print(f' Os números pares escolhidos são: {str(listaPares)}.')
    print(f' A soma dos números pares sorteados é {soma}.')


sorteia()
soma_par()
