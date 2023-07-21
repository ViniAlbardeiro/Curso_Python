    #valor do produto
preco = float(input('\n Digite o preço do produto em reais: '))
    #forma de pagamento
pay = int(input(' Para escolher a forma de pagamento, insira:'
            '\n     [1] Dinheiro/Cheque - Á vista.'
            '\n     [2] Cartão - Á vista.'
            '\n     [3] Cartão - Parcelado.'
            '\n Sua escolha: '))

if pay == 1:
    print(f'\n  Ao escolher tal forma de pagamento, ganha-se um desconto de 10%, onde o valor passa a ser de {preco*0.9:.2f} reais.')
elif pay == 2:
    print(f'Ao escolher tal forma de pagamento, ganha-se 5% de desconto, onde o valor passa a ser de {preco * 0.95} reais.')
elif pay == 3:
    print('\n           Parcelar acima de 2x, juros de 20%.')
    parcel = int(input(' Digite a quantidade de parcelas: '))
    if parcel <= 2:
        print(f'\n  Parcelando {preco} reais em {parcel}x, cada parcela vai custar {preco/parcel} reais.')
    else:
        print(f'\n  Parcelando {preco} reais em {parcel}x, cada parcela vai custar {(preco/parcel) + (preco * 0.2)} reais.')