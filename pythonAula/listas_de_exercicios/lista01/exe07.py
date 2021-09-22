'''
    Três amigos, Carlos, André e Felipe, decidiram rachar igualmente a conta de um
    bar. Faça um algoritmo para ler o total da conta e imprimir quanto cada um deve
    pagar, mas faça com que Carlos e André não paguem centavos. Ex: uma conta de
    R$101,53 resulta em R$33 para Carlos e Andre e R$35,53 para Felipe.
'''

# Essa a primeira vez que fiz eu não consegui fazer sozinho :'(

conta = float(input("Informe o valor total da conta: "))

divisao = conta/3

carlosAndre = int(divisao)
felipe = conta - carlosAndre


print(f"Carlos e André devem pagar R${carlosAndre} e Felipe deve pagar R${felipe:.2f}!")

#Confesso que não to conseguindo fazer agora dnv :p
#Fazer dps, se não não termino o resto.