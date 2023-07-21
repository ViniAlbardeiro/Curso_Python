totalSpent = qtItem1000 = 0
switch = " "
shopCart = []

while True:
    nameItem = str(input('\n Nome do Produto: ')).strip().capitalize()
    priceItem = int(input(' Preço: R$'))
    totalSpent += priceItem

    if priceItem >= 1000:
        qtItem1000 += 1
    shopCart.append([priceItem, nameItem])
    shopCart.sort()

    switch = str(input('\n Deseja continuar? [S/N]')).strip().upper()
    while switch not in "SN":
        switch = str(input('\n Deseja continuar? [S/N]')).strip().upper()
    if switch == "N":
        break

# Qual o total gasto?
print("-"*16)
print(f' No total foram gastos R${totalSpent},00')

# Quantos produtos custam mais de 1000 reais
print(f' {qtItem1000} itens custam mais de R$1000,00')

# Qual o nome do produto mais barato.
print(f' {shopCart[0][1]} é o produto mais barato')
