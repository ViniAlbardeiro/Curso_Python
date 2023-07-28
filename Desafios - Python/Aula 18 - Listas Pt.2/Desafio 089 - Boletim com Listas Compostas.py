from statistics import mean
people = []
person = []
notes = []

while True:
    name = input("\n Nome: ")
    note1 = float(input(' Nota: '))
    note2 = float(input(' Nota: '))
    notes.append(note1)
    notes.append(note2)
    person.append(name)
    person.append(notes[:])
    people.append(person[:])
    notes.clear()
    person.clear()
    cont = input(' Deseja continuar? [S/N]')
    while cont not in "SsNn":
        cont = input(' Deseja continuar? [S/N]')
    if cont in 'Nn':
        break

print('-='*40)
print('Nº', 'NOME'.center(20), 'MÉDIA'.rjust(10))
for cont1 in range(0, len(people)):
    print(cont1, people[cont1][0].center(20), str(mean(people[cont1][1])).rjust(10))
print('-='*40)
while True:
    cont = int(input(' Digite o número correspondente ao aluno para saber suas notas [999 para encerrar :)]: '))
    print(f' As notas de {people[cont][0]} são {people[cont][1]}')
    if cont == 999:
        break
