pesos_iguais = 0
todos_pesos = []
bool_test = 0
for i in range(0, 5):
    peso = float(input(' Digite seu peso: '))
    todos_pesos.append(peso)
    if todos_pesos[i-1] == todos_pesos[i]:
        bool_test += 1

if bool_test == 1:
    print('Todos os pesos são iguais.')
else:
    todos_pesos.sort()
    print(f'\n O maior peso é {todos_pesos[-1]}Kg, e o menor é {todos_pesos[0]}Kg.')
