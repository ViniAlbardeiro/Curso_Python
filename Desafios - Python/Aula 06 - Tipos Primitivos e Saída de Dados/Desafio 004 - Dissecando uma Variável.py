amarelo = '\033[33m'
roxo = '\033[35m'

n = input(roxo + '\n Digite algo: ')

print(roxo, '\n O dígito acima é numérico? ➤', amarelo, n.isnumeric())
print(roxo, ' O dígito acima é alfabético? ➤', amarelo, n.isalpha())
print(roxo, ' O dígito acima é alfanumérico? ➤', amarelo, n.isalnum())
print(roxo, ' O dígito acima é inteiro? ➤', amarelo, n.isdecimal())
print(roxo, ' O dígito acima está em letras maiúsculas? ➤', amarelo, n.isupper())
print(roxo, ' O dígito acima está em letras minúsculas? ➤', amarelo, n.islower())
print(roxo, ' O dígito acima faz parte do codigo ASCII? ➤', amarelo, n.isascii())
print(roxo, ' O dígito acima tem espaço? ➤', amarelo, n.isspace())
print(roxo, ' O dígito acima é printável? ➤', amarelo, n.isprintable())
print(roxo, ' O dígito acima é um dígito? ➤', amarelo, n.isdigit())
print(roxo, ' O dígito acima está capitalizado? ➤', amarelo, n.istitle())
