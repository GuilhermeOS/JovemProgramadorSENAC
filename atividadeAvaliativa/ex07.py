numero = int(input("Informe um número inteiro e positivo: "))

soma = 1

if type(numero) == int and numero > 0:
    for n in range(1, numero + 1):
        soma += 1/n

    print(soma)
else:
    print("Digite um número inteiro e positivo!")