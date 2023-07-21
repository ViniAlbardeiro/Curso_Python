roxo = '\033[35m'
padrao = '\033[m'

n = int(input(roxo + 'Digite um número qualquer: '))
print(f'O antecessor de \033[33m{n}\033[35m é \033[m{n-1}\033[35m e o sucessor é \033[m{n+1}')
