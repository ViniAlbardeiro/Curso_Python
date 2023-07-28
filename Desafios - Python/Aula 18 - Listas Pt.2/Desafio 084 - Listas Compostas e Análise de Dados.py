from statistics import mean
people = []
person = []
weight = []

while True:
    person.append(str(input('\n Nome: ')))
    person.append(int(input(' Massa: ')))
    people.append(person[:])
    person.clear()
    switch = str(input(' Quer continuar? [S/N] ')).upper()
    while switch not in "SN":
        switch = str(input(' Quer continuar? [S/N] ')).upper()
    if switch == "N":
        break

print('-'*60)

print(f'\n Foram cadastradas {len(people)} pessoas.\n')
for p in people:
    weight.append(p[1])
    if p[1] > mean(weight):
            print(f' {p[0].capitalize()} é pesadinho(a).')
    else:
            print(f' {p[0].capitalize()} é levinho(a).')
print(people)
