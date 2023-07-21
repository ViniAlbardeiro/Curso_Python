from math import tan, cos, sin, radians

ang = float(input('\n Digite um ângulo: '))

print(f'\n o seno deste ângulo é {(sin(radians(ang))):.2f},'
      f' o cosseno é {(cos(radians(ang))):.2f} e'
      f' a tangente é {(tan(radians(ang))):.2f}.')

