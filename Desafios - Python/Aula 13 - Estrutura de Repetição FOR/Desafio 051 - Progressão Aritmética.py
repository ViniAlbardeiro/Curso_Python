n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
l = []

for i in range(1,11):
    pa = n + i*r
    l.append(pa)
print(f'\n {l[0]} -> {l[1]} -> {l[2]} -> {l[3]}'
      f' -> {l[4]} -> {l[5]} -> {l[6]} -> {l[7]}'
      f' -> {l[8]} -> {l[9]} -> ACABOU')