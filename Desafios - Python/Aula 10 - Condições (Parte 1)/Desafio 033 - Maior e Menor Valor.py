
a = int(input('\n Digite um número: '))
b = int(input('\n Digite outro número: '))
c = int(input('\n Digite outro número: '))


if b <= a >= c:
    print(f'O maior valor digitado foi {a}.')

if a <= b >= c:
    print(f'O maior valor digitado foi {b}.')

if a <= c >= b:
    print(f'O maior valor digitado foi {c}.')

if b >= a <= c:
    print(f'O menor valor digitado foi {a}.')

if a >= b <= c:
    print(f'O menor valor digitado foi {b}.')

if a >= c <= b:
    print(f'O menor valor digitado foi {c}.')
