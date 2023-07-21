
numWrite = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numEntry = int(input('\n Digite um número entre 0 e 20: '))

while numEntry > 20 or numEntry < 0:
    numEntry = int(input(' Tente novamente. Digite um valor entre 0 e 20: '))
print(f'\n Você digitou o número {numWrite[numEntry]}')
