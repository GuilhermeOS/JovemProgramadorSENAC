from matilha import *
import time



for cachorros in range(0, 21):
    dog = Matilha(nome = "Dog" + str(cachorros), idade = Matilha.idades())

    print(f"O {dog.nome} tem {dog.idade} anos de idade!")
    time.sleep(0.6)
