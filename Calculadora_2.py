"""
Created on Sun Jun 27 20:38:50 2021

@author: RyOoxNaY
"""
def suma():
    n1 = int(input("Ingresa el primer dígito: "))
    n2 = int(input("Ingresa el segundo dígito: "))
    print("\r")
    print("El resultado es: ", n1+n2)
def resta():
    n1 = int(input("Ingresa el primer dígito: "))
    n2 = int(input("Ingresa el segundo dígito: "))
    print("\r")
    print("El resultado es: ", n1-n2)
def multi():
    n1 = int(input("Ingresa el primer dígito: "))
    n2 = int(input("Ingresa el segundo dígito: "))
    print("\r")
    print("El resultado es: ", n1*n2)
def divi():
    n1 = int(input("Ingresa el primer dígito: "))
    n2 = int(input("Ingresa el segundo dígito: "))
    print("\r")
    print("El resultado es: ", n1/n2)
c = 1
while c == 1:
    print("             ******* BIENVENIDOS  ********")
    print("\r")
    print("1) Suma   2) Resta   3) Multiplicación 4)Divición")
    a = int(input())
    if a == 1:
        suma()
    elif a == 2:
        resta()
    elif a == 3:   
        multi()
    elif a == 4:
        divi()
    else:
        print("Ingrese una opción valida...")
    c = int(input(" 1) Seguir   0)Salir "))

