from random import choice

a = input('\n Digite o nome do primeiro aluno: ')
b = input(' Digite o nome do segundo aluno: ')
c = input(' Digite o nome do terceiro aluno: ')
d = input(' Digite o nome do quarto aluno: ')

print(f'\n O aluno sorteado foi: \033[0;36m {choice([a,b,c,d])}!')
