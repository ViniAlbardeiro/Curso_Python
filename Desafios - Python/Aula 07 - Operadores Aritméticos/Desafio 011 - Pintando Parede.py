w = float(input('\n Digite a largura de sua parede: '))
h = float(input(' Digite a altura de sua parede: '))
t = int(input(' Digite quantos m² a tinta a ser utilizada rende por litro em média: '))

print(f'\n  '
      f'Você vai precisar de mais ou menos {(w*h)/t:.2f}l de tinta')
