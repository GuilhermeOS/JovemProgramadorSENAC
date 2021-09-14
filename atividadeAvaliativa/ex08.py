numero = int(input("Quantas pessoas ?"))
soma = 0
idadeTotal = 0

for x in range(0, numero):
    idade = int(input("Qual a idade ? "))

    if idade >= 18:
        soma += 1
        idadeTotal += idade

print(f"O total de pessoas maiores de idade é {soma}\nA média de idade dos adultos é {idadeTotal/soma:.2f} anos")

# TERMINAR EM CASA