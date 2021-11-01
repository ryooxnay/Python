# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 01:34:16 2021

@author: USER
"""
def intro():
    import time 
    print("Este es el famoso juego de la moneda")
    time.sleep(2)
    print("************************************")
    time.sleep(2)
def juego():
    import random
    import time
    intro()
    tiros = int(input("Ingrese cuantas veces desea lanzar la moneda. \n:"))
    cara = 0
    cruz = 0
    tiro = 1
    while tiro < tiros + 1:
        moneda = random.randint(1,2)
        if moneda == 1:
            cara = cara+1
        elif moneda == 2:
            cruz = cruz + 1
        tiro = tiro + 1 
    print("Se realizarón ", tiros, " tiros.")
    time.sleep(2)
    print("De los cuales ", cruz," fueron cruz.")
    time.sleep(2)
    print("Y ", cara," fueron cara.")

juego()


    

