def cartas():
    import random
    from random import sample
    car = ["1","2","3","4","5","6","7","8","9","J","Q","K"]
    tip = ["Corazones","Espada","Diamantes","Treboles"]
    for i in car:
        uno = i, tip[0]
        dos = i, tip[1]
        tres = i, tip[2]
        cuatro = i, tip[3]
        final = list(uno)*list(dos)*list(tres)*list(cuatro)
        
        print(final)
        
             
cartas()
