'''
    Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das
    seguintes categorias:
        a. infantil A = 5-7 anos
        b. infantil B = 8-10 anos
        c. juvenil A = 11-13 anos
        d. juvenil B = 14-17 anos
        e. adulto = maiores de 18 anos
'''

quantidadeNadadores = int(input("Informe a quantidade de nadadores da competição: "))

for nadadores in range(0, quantidadeNadadores):
    idade = int(input("Informe a idade do nadador: "))

    if idade <= 7:
        print("Categoria infantil A")
    elif idade <= 10:
        print("Categoria infantil B")
    elif idade <= 13:
        print("Categoria juvenil A")
    elif idade <= 17:
        print("Categoria juvenil B")
    else:
        print("Categoria adulto") 