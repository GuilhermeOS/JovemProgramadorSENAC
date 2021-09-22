'''
    A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade 
    de broas a cada dia. Cada pãozinho custa R$0,12 e a broa custa R$1,50. Ao final
    do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos),
    e quanto deve guardar numa conta de poupança (10% do total arrecadado). Você foi
    contratado para fazer os cálculos para o dono. Combase nestes fatos, faça um 
    algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados
    solicitados.
'''

quantidadePaes = int(input("Quantidade de pães franceses vendidos no dia: "))
quantidadeBroas = int(input("Quantidade de broas vendidas no dia: "))

valorArrecadado =  (quantidadePaes * 0.12) + (quantidadeBroas * 1.50)

guardar = valorArrecadado * 0.10

print(f"Foram arrecadados R${valorArrecadado:.2f} com a venda dos pães e broas do dia!")
print(f"Assim, deve ser guardado R${guardar:.2f} na poupança!")