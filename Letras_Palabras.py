Metodos de formato de combercion de mayusculas a minusculas

****** Primera letra en mayusculas

cadena = "hola mundo"
print(cadena.capitalize())
# Hola mundo

****** Convertir una cadena a minusculas

cadena = "Hola mundo"
print(cadena.lowe())
# hola mundo

****** Convertir una cadena a mayusculas

cadena = "Hola mundo"
print(cadena.upper())
# HOLA MUNDO

****** Convertir mayusculas a minusculas y viceversa

cadena = "Hola Mundo"
print(cadena.swapcase())
# hOLA mUNDO

****** Convertir una cadena en formato Titulo
cadena = "hola mundo"
print(cadena.title())
# Hola Mundo

****** Longitud en cadenas
cadena = "banana"
print(len(cadena))
# 6

****** 
****** Centrar un texto 
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.center(50,"="))                  # "%", lo de comillas es el caracter que se pondra. 
# ==================Bienvenido a mi aplicación=================

****** Alinear texto a la izquierda
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.ljust(50,"="))
# Bienvenido a mi aplicación=======================

****** Alinear texto a la derecha
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.rjust(50,"="))
# =======================Bienvenido a mi aplicación

****** Rellenar un texto anteponiendo ceros
n_f = 1592
print(str(n_f).zfill(12))
#000000001592

****** Como comparar dos cadenas String sin inportar si son mayusculas y minusculas

a = input("Ingrese una contraseña : ")
c = 1
while c > 0:
    b = input("Ingrese la contraseña: ")
    if a.lower() == b.lower():
        print("La contraseña es correcta.")
    else:
        print("la contraseña es incorrecta")
    c = int(input("1) Desea intentar otra vez 0) Salir  : "))

******* Obtener las primeras palabras de una frase
c = 1
while c > 0:
    p = input("Ingrese su nombre con apeidos : ")
    o = p.split(" ")
    q = " "
    for i in o:
        q += i[0]
    print(q)
    c = int(input("1) Ingresar otra vez  0) Salir : "))

