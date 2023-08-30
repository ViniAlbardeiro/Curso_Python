student = {}

student["name"] = str(input('\n Nome: '))
student["mean"] = float(input(f" Média de {student['name'].capitalize()}: "))

if student["mean"] >= 5:
    print(f'\n {student["name"]} recebeu a aprovação.')
else:
    print(f'\n {student["name"]} não recebeu a aprovação.')