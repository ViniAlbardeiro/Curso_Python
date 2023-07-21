nota1 = float(input('\n Primeira nota: '))
nota2 = float(input(' Segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7.0:
    print(f'Com a média {media:.1f}, foi APROVADO.')
elif 5.0 <= media >= 6.9:
    print(f'Com a média {media:.1f}, ficou de RECUPERAÇÃO.')
elif media <= 4.9:
    print(f'Com a média {media:.1f}, foi REPROVADO.')