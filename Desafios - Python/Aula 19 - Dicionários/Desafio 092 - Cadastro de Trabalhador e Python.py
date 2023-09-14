from datetime import date

anoAtual = int(str(date.today())[0:4])
pessoa = dict()
pessoa["nome"] = input(" Nome: ")
pessoa["anoDeNascimento"] = int(input(" Data de nascimento: "))
pessoa["idade"] = anoAtual - pessoa["anoDeNascimento"]

if pessoa["idade"] >= 18:
    carteiraTrabalho = input(" Tens carteira de trabalho? ")
    if carteiraTrabalho in "Simsim":
        pessoa["CTPS"] = int(input(' Número CTPS: '))
        pessoa["primeiroRegistro"] = int(input(" Ano da primeira contratação: "))
        pessoa["salario"] = int(input(" Valor salarial: "))
        pessoa["aposentadoria"] = (pessoa["primeiroRegistro"] - pessoa["anoDeNascimento"]) + 35

print(" _______________________________________________")

for Chave, Valor in pessoa.items():
    print(f' A chave ´{Chave}´ tem valor ´{Valor}´.')
