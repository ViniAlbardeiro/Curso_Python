l = []
soma = 0

for i in range(0, 500):
    if i % 3 == 0 and i % 2 == 1:
        soma += i
        l.append(i)

print(soma)
print(len(l))

#Obtive ajuda!