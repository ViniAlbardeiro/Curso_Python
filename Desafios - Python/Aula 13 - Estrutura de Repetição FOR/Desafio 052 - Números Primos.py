n = int(input('Digite um número: '))
l = []

for i in range(1, n+1):
     if n % i == 0:
         l.append(i)
if len(l) > 2:
    print(f'\033[32m Os divisores de \033[35m{n}\033[32m são \033[35m{l}'
          f'\033[32m, logo, \033[35m{n}\033[32m não é um número primo.')
else:
    print(f'\033[32m Os divisores de \033[35m{n}\033[32m são \033[35m{l}'
          f'\033[32m, logo, \033[35m{n}\033[32m é um número primo.')
