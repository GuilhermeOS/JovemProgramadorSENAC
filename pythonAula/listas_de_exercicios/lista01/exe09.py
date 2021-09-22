'''
    A empresa Hipotheticus paga R$10 por hora normal trabalhada, e R$15  por hora
    extra. Faça um algoritmo para calcular e imprimir o salário bruto e o salário
    líquido de um determinado funcionário. Considere que o salário líquido é igual
    ao salário bruto, descontando-se 10% de impostos.
'''

horasTrabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))

salarioMensal = horasTrabalhadas * 10

extra = str(input("O funcionário fez trabalho extra ? (S/N)"))

if extra == "S" or extra == "s":
    horaExtra = int(input("Quantas horas extras ? "))

    salarioExtra = horaExtra * 15
else:
    pass

salarioBruto = salarioMensal + salarioExtra

salarioLiquido = salarioBruto - (salarioBruto * 0.10)

print(f"O salário bruto do funcionário é R${salarioBruto:.2f}!\nCom os descontos fica R${salarioLiquido:.2f}!")
