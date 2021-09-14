b1 = None
b2 = None
b3 = None

if (b1 == True):
    c1 = True
else:
    if (b2 == True):
        if (b3 == True):
            c2 = True
        else:
            c3 = True
        c4 = True
c5 = True

# a - se b1 for true(imagino que V seja verdadeiro) só será executada a
# primeira parte do if. E o c5 que está fora do laço.

# b - se b1 for False, b2 True e b3 False, será excutado o primeiro if
# dentro do else. mais especificamente as linhas 8 e 13, ou seja o c4 vai 
# receber True, apenas. E o c5 que está fora do laço.

# c - já se b3 for True também serão executados os comando das linhas 7 até
# o final do código. Ou seja, do primeiro else pra frente.

# d - b1 = False; b2 = False; b3 = False

'''
    Tá errado, corrigir depois
'''