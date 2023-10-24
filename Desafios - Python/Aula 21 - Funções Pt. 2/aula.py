# _________________________________________________________________________________________________________________________________________________________________

# Usar comando help() para um "manual de instruções" de algum comando
print('__'*40)
help(print)  # Ou escrever isso no python console

# _________________________________________________________________________________________________________________________________________________________________

# Docstrings é escrita logo abaixo de "def.", e serve para comentar sobre a função criada.
# Para declarar um docstring, basta escrever """...""".
# Para acessar a docstring, usa-se o comando help()
print('__'*40)


def contador(i, f, p):
    """
    Faz uma contagem de números e mostra na tela
    :param i: Início do contador
    :param f: Fim do contador
    :param p: Passo/Intervalo do contador
    :return: Sem retorno
    Criada por Vinicin da Bala Chita
    """
    for numero in range(i, f+1, p):
        print(numero, end='...')
    print('Fim')


help(contador)
contador(0, 10, 2)

# ______________________________________________________________________________________________________________________________________________________________

# Para tornar os parâmetros de uma função opcional, basta que ao criar a função, iguale o(s) parâmetro(s) a 0.
print('__'*40)


def soma(a, b, c = 0):
    s = a + b + c
    print(s)


soma(2, 5)
print('__' * 40)
# ______________________________________________________________________________________________________________________________________________________________

# Escopo de variáveis: Há dois tipos, a var GLOBAL e LOCAL


# noinspection PyShadowingNames
def teste(b):
    a = 8
    b += 5
    c = 2
    print(f' Na função teste, A tem valor {a}.')
    print(f' Na função teste, B tem valor {b}.')
    print(f' Na função teste, C tem valor  {c}.')


a = 4
teste(a)
print(f' Fora, A vale {a}')
# print(f' Fora, B vale {b}')
# print(f' Fora, C vale {c}')

# Note que B e C, por estarem na função, elas não podem ser chamadas fora da função, senão dá erro.
# Isso ocorre, porque elas são variáveis de escopo local, ou seja, só funcionam na função.
# O que difere na variável A, pois há dois escopos para a mesma variável.
# A de escopo global, foi declarado fora, foi usada para definir B na função teste. e é completamente diferente da variável A que está na função teste.
# Logo, A de fora vale 4, A de dentro vale 8, B é A de fora + 5, o qual é igual a 9, e por fim, C equivale a 2.
