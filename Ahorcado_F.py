# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:11:09 2021

@author: USER
"""
def uno():
    print("   +---+")
    print("   |   |")
    print("       |")
    print("       |")
    print("       |")
    print("       |")
    print("       |")
    print("========")
def dos():
    print("   +---+")
    print("   |   |")
    print("   O   |")
    print("       |")
    print("       |")
    print("       |")
    print("       |")
    print("========")
def tres():
    print("   +---+")
    print("   |   |")
    print("   O   |")
    print("   |   |")
    print("       |")
    print("       |")
    print("       |")
    print("========")
def cuatro():
    print("   +---+")
    print("   |   |")
    print("   O   |")
    print("   |\  |")
    print("       |")
    print("       |")
    print("       |")
    print("========")
def cinco():
    print("   +---+")
    print("   |   |")
    print("   O   |")
    print("  /|\  |")
    print("       |")
    print("       |")
    print("       |")
    print("========")
def seis():
    print("   +---+")
    print("   |   |")
    print("   O   |")
    print("  /|\  |")
    print("  /    |")
    print("       |")
    print("       |")
    print("========")
def siete():
    print("   +---+")
    print("   |   |")
    print("   O   |")
    print("  /|\  |")
    print("  / \  |")
    print("       |")
    print("       |")
    print("========")
def ocho():
    
    print("_____¤¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¤_")
    print("___¤¶¶¶¶¶¶¶¶¤¤¤¤¤¶¶¶¶¶¶¶¶¤_")
    print("__¤¶¶¶¶¶¶¶¤¤¤¤¤¤¤¤¤¶¶¶¶¶¶¶¤_")
    print("_¤¶¶¶¶¤¶¶¶¶¶¤¤¤¤¤¶¶¶¶¶¤¶¶¶¶¤_")
    print("_¤¶¶¶¶¶¤¶¶¶¶¶¤¤¤¶¶¶¶¶¤¶¶¶¶¶¤_")
    print("_¤¶__¤¶¶¶¶¶¶¶¶¤¶¶¶¶¶¶¶¶¤__¶¤_")
    print("_¤¶_____¤¶¶¶¶¶¶¶¶¶¶¶¤_____¶¤_")
    print("_¤¶_______¤¶¶¶¶¶¶¶¤_______¶¤_")
    print("__¤¶__________¶¶_________¶¤_")
    print("___¤¶¶________¶¶________¶¶¤_")
    print("____¤¶¶¶¶¶¶¤______¤¶¶¶¶¶¶¤_")
    print("_¤¶¶¤¤¶¶¶¤_________¤¶¶¶¶¤¤¶¶¤_")
    print("___¤¶¶¶¶__¶¶¶*¶*¶¶¶__¶¶¶¶¤_")
    print("__________¤¶¶¶¶¶¶¶¤_")
    print("___________¤¶¶¤¶¶¤_")
    print("___________¤¶¤¤¤¶¤_")
    print("___________¤¶¶¤¶¶¤_")
    print("_____________¶¤¶_")
def ganar():
    print("          (0 0) ")
    print("  ---oOO-- (_) ----oOO---")
    print("╔═════════════════════════╗ ")
    print("║ ♥ Felicidades Ganaste ♥ ║ ")
    print("╚═════════════════════════╝ ")
    print("    ------------------- ")
    print("          |__|__| ")
    print("           || || ") 
    print("          ooO Ooo ")
def intro():
    import time
    print("Bienvenido al jego del AHORACADO => B)")
    time.sleep(1)
    print("El juego es simple, tentras que ir escribiendo una letra a la vez")
    time.sleep(1)
    print("para ir descbriendo qe palabra esta formada.")
    time.sleep(1)
    print("Si no adivinas la letra se ira acompletando ")
    time.sleep(1)
    print("un muñeco el cual quedara ahorcado...")
    time.sleep(1)
    print("Serte amigo (づ￣ 3￣)づ ")
def juego():
    import time
    uno()
    time.sleep(2)
    dos()
    time.sleep(2)
    tres()
    time.sleep(2)
    cuatro()
    time.sleep(2)
    cinco()
    time.sleep(2)
    seis()
    time.sleep(2)
    siete()
    time.sleep(2)
    ocho()
def jue():
    import random
    LAniTerr = ["perro","conejo","caballo","elefante","tigre",
    "bufalo","rinoceronte","chita","burro","gato","lobo","vibora"]
    LFru = ["manzana","durazno","naranja","papalla","jitomate"
            ,"piña","mandarina","sandia","guayaba","platano"]
    LComi =["arroz","tacos","pizza","tamales","garnachas","sopa"
            ,"torta","pipian","cereal","pastel","gelatina"]
    intro()
    lista = random.randint(1,3)
    print (lista)
    if lista == 1:
        pala = random.choice(LAniTerr)
        print("La palabra a adivinar cuenta con: ", len(pala), " letras y es un animal.")
        n = len(pala)
        print("      ", n * "* ")
        uno()
        inten = input("Ingresa una letra : ")
        if inten == pala:
            ganar()
        else:
            uno()
        
    elif lista == 2:
        pala = random.choice(LFru)
        print("La palabra a adivinar cuenta con: ", len(pala), " letras y es una fruta.")
        n = len(pala)
        print("      ", n * "* ")
        inten = input("Ingresa una letra : ")
        if inten == pala:
            ganar()
        else:
            uno()
    elif lista == 3:
        pala = random.choice(LComi)
        print("La palabra a adivinar cuenta con: ", len(pala), " letras y es una comida.")
        n = len(pala)
        print("      ", n * "* ")
        inten = input("Ingresa una letra : ")
        if inten == pala:
            ganar()
        else:
            uno()

    

    
jue()
