class Flor():

    def __init__(self, tipoFlor, quantidade):
        self.tipoFlor = tipoFlor
        self.quantidade = quantidade

    def flores():
        flores = {
            "Rosa" : 10.00,
            "Girassol" : 8.50, 
            "Hortênsia" : 15.00, 
            "Tulipa" : 12.00, 
            "Dália" : 13.25, 
            "Lírios" : 7.80, 
            "Cravos" : 9.99
        }

        return flores

    def menu():
        print("--- {:^40} ---".format("FLORICULTURA"))
        print("--- {:^40} ---".format("FLORES DISPONÍVEIS"))
        
        flores = Flor.flores()
        
        for produto, preco in flores.items():
            print(f"{produto:10} - R${preco:.2f}")
        
        #Uma iteração dicionário feita com for itera somente as keys. Por isso nunca será visível os valores.
        #Uma das soluções para isso é usar o items, como feito acima, o método .items devolve as chaves e 
        #valores em sequencia.
    
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

menu = Flor.menu()
buque = Flor.montaBuque()
print(buque)