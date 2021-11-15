def bugs():
    import random
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    print("¿Cuanto es: ", num1, " + ", num2, " = ")
    res = int(input())
    if res == num1+num2:
        print("Tu respuesta es correcta")
    else:
        print("Tu respuesta es incorrecta")

def juego():
    otro = 1
    while otro == 1:
        if otro == 1:
            bugs()
        else:
            break
        otro = int(input("1) Jugar otra vez  2) No jugar  \n= "))
juego()
