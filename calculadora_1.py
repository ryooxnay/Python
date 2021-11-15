c = 1
while c == 1:
    print("***** BIENVENIDOS ******")
    print(" ")
    print("1) Suma  2) Resta  3) Multiplicación  4) Divición")
    a = int(input())
    if a == 1:
        b = int(input())
        print("+")
        d = int(input())
        print(" ")
        print(" R = ",  b + d)
        print(" ")
    elif a == 2:
       b = int(input())
       print("-")
       d = int(input())
       print(" ")
       print(" R = ", b - d)
       print(" ")
    elif a == 3:
       b = int(input())
       print("*")
       d = int(input())
       print(" ")
       print(" R = ", b * d)
       print(" ")
    elif a == 4:
       b = int(input())
       print("/")
       d = int(input())
       print(" ")
       print(" R = ", b - d)
       print(" ")
    else:
        print("Ingrese una opcion valida")
    c = int(input("1) Seguir  0)Salir : "))
    


import math
num = 12.8
print(math.floor(num), end=" ")
print(math.ceil(num))
