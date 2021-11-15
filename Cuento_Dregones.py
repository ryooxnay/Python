# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 01:42:01 2021

@author: USER
"""
def juego_dragon1():
    
    import random
    import time
    def tim():
        time.sleep(3)
    def intro():
        print("Estas en una tierra llena de dragones." )
        tim()
        print("Frente de ti hay dos cuevas. en una de ellas")
        tim()
        print("esta un dragon generos, amigable que compartira su tesoro")
        tim()
        print("y en la otra esta un dragon codicioso y hambrieto")
        tim()
        print(" que te devorara en seguida \n")
    def eliC():
        cueva = " "
        while cueva != 1 and cueva != 2:
            cueva = int(input("A que cuava quieres entrar? \n 1)Cueva 1 \n 2)Cueva 2  \n  \n : "))
        return cueva
    def exploCue(eliC):
        print("Te aproximas a la cueva...")
        tim()
        print("Es oscura y pelusnante...")
        tim()
        print("Un dragon aparece frente de ti...")
        tim()
        cuevaAmi = random.randint(1,2)
        if eliC == cuevaAmi:
            print("Te regala su tesoro.")
            tim()
        else:
            print("Te devora de un mordisco.")
            tim()
    otro = "si"
    while otro == "si" or otro == "s":
        intro()
        cuevaAmi = eliC()
        exploCue(cuevaAmi)
        otro = input("¿Quieres jugar de nuevo? \n (si  o  no) \n : ")
        
juego_dragon1()
