# Entrada do nome da cidade.
text = input('\n Em que cidade você nasceu? ')

# Remoção de espaços nas extremidades, tornando o nome maiúsculo e dividindo o nome em listas.
text1 = (text.strip().upper().split())

# Identificando se existe o termo 'SANTO' na palavra, onde retorna True ou False.
text2 = bool(text1[0].find('SANTO'))

# Exibe na tela o contrário do resultado da var 'text1'.
print(not text2)

# Método do Guanabara

#cid = str(input('Em que cidade você nasceu? ')).strip()
#print(cid[:5].upper() == 'SANTO')

#
