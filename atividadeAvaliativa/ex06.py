'''
i = 0

while i < 10:
    print(i)

    if i == 7:
        break
'''

# Tá errado.

# Faria assim:

i = 0

while i < 10:
    print(i)

    i += 1 #Assim o i será acrescentado de 1 até chegar ao número 7, sendo possível parar a execução.

    if i == 7:
        break
