from montaBuque import Flor

def montaBuque():
    quantidade = int(input("Informe a quantidade de flores desejadas: "))
    valor = {}
    flores = Flor.flores()
    for _ in range(0, quantidade):
        flor = str(input("Informe a flor desejada: "))
        if flor in flores:
            valor[flor] = flores[flor]

    print(valor)
    valorTotal = sum(valor.values())

    return valorTotal

#Ta meio errado, arrumar dps
