'''
    Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o
    início do ano. Esqueça a questão dos anos bissextos e considere sempre que um 
    mês possui 30 dias.
'''


dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))

dias = (mes * 30) + dia

print(f"Já se passaram {dias} dias desdo o início do ano!")