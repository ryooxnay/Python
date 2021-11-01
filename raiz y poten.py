# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 09:29:52 2021

@author: RyOoxNaY
"""
def raiz():
    import math
    n1 = int(input("Ingrese un número: " ))
    n2 = math.sqrt(n1)
    print("El resultado es: ", str(n2))
    print("\r")
def poten():
    n1 = int(input("Ingrese un digito: "))
    n2 = int(input("Ingrese su potencia: "))
    print("El resultado es: ", str(n1**n2))
    print("\n")

x = 1
while x == 1:
    print("***** BIENVENIDOS ******")
    print(" ")
    print("1) Raiz cuadrada  2) Potencia ")
    a = int(input())
    if a == 1:
        raiz()
    elif a == 2:
        poten()
    else:
        print("Ingrese una opcion valida")
    x = int(input("1) Seguir  0)Salir : "))

