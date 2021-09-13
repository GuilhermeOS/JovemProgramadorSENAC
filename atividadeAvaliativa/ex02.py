import datetime

nascimento = int(input("Informe o ano que vc nasceu: "))

anoAtual = datetime.date.today().year

idade_em_anos = anoAtual - nascimento

idade_em_meses = idade_em_anos * 12

idade_em_semanas = idade_em_meses * 4

idade_em_dias = idade_em_meses * 30

print(f"Você tem {idade_em_anos} anos de idade!")
print(f"Você tem {idade_em_meses} meses de idade!")
print(f"Você tem {idade_em_semanas} semanas de idade!")
print(f"Você tem {idade_em_dias} dias de idade!")
