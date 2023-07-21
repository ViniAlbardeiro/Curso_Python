# Descobrir o salário
salario = int(input('\n\033[34m Qual o seu salário? '))

# Descobrir o valor do empréstimo
emprestimo = int(input(' O quanto você quer emprestado? '))

# Descobrir em quantos anos ele vai pagar
tempo = int(input(' Em quantos anos deseja pagar o empréstimo? '))

# Calcular prestação mensal
prestacao = emprestimo / (tempo*12)

# Condição de possibilidade de empréstimo (prestação <= (salario*0.3))

if prestacao <= (salario*0.3):
    print(f'\n\033[32m Parabéns, seu pedido de empréstimo foi aceito e cada '
          f'parcela custará R${prestacao:.2f}.')
else:
    print('\n\033[31m Sinto em informar, mas seu pedido de empréstimo foi negado. =(')