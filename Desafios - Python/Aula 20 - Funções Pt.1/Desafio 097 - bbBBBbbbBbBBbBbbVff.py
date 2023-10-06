def linha(txt):
    print('_', '_'*len(txt), '_')
    print(' ', txt)
    print('_', '_'*len(txt), '_')


while True:
    linha(str(input(' Digite alguma coisa: ')).title())
    resposta = input(' Quer continuar? [S/N]: ')
    if resposta in 'Nn':
        break
