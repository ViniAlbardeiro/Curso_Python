from random import shuffle

a = input('\n Digite o nome de um aluno: ')
b = input(' Digite outro nome: ')
c = input(' Digite outro nome: ')
d = input(' Digite outro nome: ')

g = [a, b, c, d]
shuffle(g)

print(f'\n A ordem de apresentação dos alunos será {g}')
