'''
    O cardápio de uma lanchonete é o seguinte:
        a. Especificação        código           preço
        b. Cachorro Quente      100              R$1,20
        c. Bauru Simples        101              R$1,30
        d. Bauru com ovo        102              R$1,50
        e. Hambúrguer           103              R$1,20
        f. Cheeseburguer        104              R$1,30
        g. Refrigerante         105              R$1,00

    Escreva um algoritmo que leia o código do item pedido, a quantidade e calcule o
    valor a ser pago por aquele lanche. Considere que a cada execução somente será
    calculado um item.
'''

# No curso a professora não passa biblioteca, então vou tentar aprender agora.
# Aqui vou usar só para fazer o cardápio msm, não precisa, mas sla, só para praticar
cardápio = {
    "Cachorro Quente 100" : "R$1,20",
    "Bauru Simples   101" : "R$1,30",
    "Bauru com ovo   102" : "R$1,50",
    "Hambúrguer      103" : "R$1,20",
    "Cheeseburguer   104" : "R$1,30",
    "Refrigerante    105" : "R$1,00",
}

for produto, valor in cardápio.items():
    print(f"{produto} : {valor}")

# Dale, deu certo.
# Tem que usar o items() ali pq na iteração com for só é percorrida as chaves do
# dicionário, ai o items faz percorrer chave e valor.

pedido = int(input("Informe o código do produto desejado: "))
quantidade = int(input("Informe a quantidade desejada: "))
valorPagar = 0

if pedido == 100 or pedido == 103:
    valorPagar = quantidade * 1.20
elif pedido == 101 or pedido == 104:
    valorPagar = quantidade * 1.30
elif pedido == 102:
    valorPagar = quantidade * 1.50
else:
    valorPagar = quantidade * 1

print(f"O valor final do seu pedido é R${valorPagar}!")
