

def menu():
    print('-' * 50)
    print('Sistema De Cadastros em Python'.center(40))
    print('-' * 50)
    print('1. Ver pessoas cadastradas')
    print('2. Cadastrar pessoa')
    print('3. Sair do sistema')
    print('-' * 50)


def cadastro(nome, idade):
    pessoa = [nome, idade]
    pessoas = list()
    pessoas.append(pessoa)
    return pessoa


def escrever(texto):
    with open(r"C:\Users\Vinicius\Desktop\desafio115.txt", "a") as arquivo:
        arquivo.write(str(texto)+"\n")
        arquivo.close()


def leitura():
    with open(r"C:\Users\Vinicius\Desktop\desafio115.txt", "r") as arquivo:
        leitura = arquivo.read()
        print(leitura)
        arquivo.close()
