'''
    Um banco concederá um crédito especial aos seus clientes, variável com o saldo
    médio no último ano. Faça um algoritmo que leia o saldo médio de um cliente
    e calcule o valor do crédito de acordo com a tebela abaico. Mostre uma mensagem
    informando o saldo médio e o valor de crédito.
        a. saldo médio      Percentual
        b. de 0 a 200       nenhum crédito
        c. de 201 a 400     20% do valor do saldo médio
        d. de 401 a 600     30% do valor do saldo médio
        e. acima de 601     40% do valor do saldo médio
'''

saldoMedio = float(input("Informe o seu saldo médio do último ano: R$"))

if saldoMedio <= 200:
    print("Infelizmente você não conseguiu crédito!")
elif saldoMedio <= 400:
    credito = saldoMedio * 0.20
    print(f"Você tem direito a R${credito} de saldo!")
elif saldoMedio <= 600:
    credito = saldoMedio * 0.30
    print(f"Você tem direito a R${credito} de saldo!")
else:
    credito = saldoMedio * 0.40
    print(f"Você tem direito a R${credito} de saldo!")
