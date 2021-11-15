def cartas():
    import random
    car = ["1","2","3","4","5","6","7","8","9","J","Q","K"]
    tip = ["Corazones","Espada","Diamantes","Treboles"]
    lis = random.randint(1,4)
    if lis == 1:
        print(random.sample(car,1), tip[0])
    elif lis == 2:
        print(random.sample(car,1), tip[1])
    elif lis == 3:
        print(random.sample(car,1), tip[2])
    else:
        print(random.sample(car,1), tip[3])
def juego():
    intentos = int(input("Ingrese cuantas cartas quiere = "))
    if intentos > 48:
        print("Son solo 48 cartas. Ingrese otra cantidad : ")
        intentos = int(input("Ingrese cuantas cartas quiere = "))
    while intentos > 0:
        cartas()
        intentos = intentos - 1
juego()
