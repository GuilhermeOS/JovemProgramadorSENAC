'''
    O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva
    um algoritmo que leia o peso do prato montado (em quilos) e imprima o valor a 
    pagar. Assuma que a balança já desconte o peso do prato.
'''

pesoPrato = float(input("Informe o peso do prato: "))

print(f"O valor total a ser pago é de R${pesoPrato * 12:.2f}!")