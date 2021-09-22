'''
    Faça um algoritmo para ler o salário de um funcionário e aumentá-lo em 15%.
    Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário
    com o aumento e o salário final.
'''

salarioMensal = float(input("Informe o seu salário mensal: R$"))

aumentoSalario = salarioMensal + (salarioMensal * 0.15)

descontoImposto = aumentoSalario - (aumentoSalario * 0.08)

print(f"O seu salário de R${salarioMensal} agora é de R${aumentoSalario}!")
print(f"Com os descontos devido a impostos é de R${descontoImposto}!")