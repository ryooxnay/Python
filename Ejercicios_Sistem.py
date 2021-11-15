"""
Created on Sun Jul  4 00:34:28 2021

@author: Ryooxnay
"""
"""
Abrir símbolo del sistema
CD C:\Python37-32\Scripts
pip install pillow
pip install pyautogui
"""
#Para mandar un mesajes
"""

import pyautogui
import time
time.sleep(5);
f = open("te.txt", "r")
for i in f:
    pyautogui.typewrite(i)
    pyautogui.press("enter")
"""
# para saber el nombre del ordenador y de la direccion ip
def ip():
    import socket
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("El nombre de tu ordenador es: ", hostname)
    print("Tu dirección IP es: ", ip)


#Para pasar numeros a numero binario
def bi():
    bi = ""
    decimal = int(input("Introdusca un dígito :" ))
    while decimal // 2 != 0:
        bi = str(decimal % 2) + bi
        decimal = decimal // 2
    print(str(decimal) + bi)
#pip install --user pyautogui

#para adivinidar un numero random
def adivNum():
    import random
    intentosR = 0
    Nombre = input("Hola ¿Como te llamas? : ")
    num = random.randint(1, 20)
    print("Bueno ", Nombre, " estoy pensando en un número.. ")
    while intentosR < 6:
        estimacion = int(input("Intenta adivinar: "))
        intentosR = intentosR + 1
        if estimacion < num:
            print("Tu estimacion es muy baja. ")
        elif estimacion > num:
            print("Tu estimacion es muy alta. ")
        elif estimacion == num:
            print("Buen trabajo ", Nombre, " ¡Has adivinado con ", intentosR, " intentos")
            break
    if estimacion != num:
        print("Pues ", Nombre, " El numero que estaba ensando era el: ", num)
  
adivNum()
def form_print():
    print("hola \ mundo")
    print("hola \\ mundo")
    print("\' Hola mundo \'")
    print("\" Hola mundo \"")
    print(" Hola \n Mundo")
    print("Hola \t Mundo")



