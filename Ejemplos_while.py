'''
o = 1
while o > 0:
    a = int(input("Ingrese su edad : "))
    if a >= 18:
        print("Usted ya es mayor de edad.")
    else:
        print("Usted es un menor de edad.")
    o = int(input("%n => Preguntar otra vez, 0 => Salir  : "))

a = input("Ingrese una contraseña : ")
c = 1
while c > 0:
    b = input("Ingrese la contraseña: ")
    if a.lower() == b.lower():
        print("La contraseña es correcta.")
    else:
        print("la contraseña es incorrecta")
    c = int(input("1) Desea intentar otra vez 0) Salir  : "))
    
d = 1
while d > 0:
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese le segundo valor : "))
    c = a * b
    if c == 0:
        print("Error, no se puede dividir entre 0")
           
    else:
        print("La divicion es ", a/b) 
    d = int(input("1) Ingresar otra vez  0) Salir : "))

b = 1
while b > 0:
    a = int(input("Ingrese un numero : "))
    if a%2 == 0:
        print("Eso es par")
    else:
        print("Es inpar")
    b = int(input("1) Ingresar otra vez  0) Salir : "))

c = 1
while c > 0:
    a = int(input("Ingrese su edad : "))
    b = int(input("Ingrese su ingreso mensual : "))
    if a > 18:
        if b >= 1000:
            print("El usuario tiene que tributar")
        else:
            print("El usuario es mayor de edad, pero cuenta con el salario requerido")
    else:
        print("El usuario no cumple los requisitos")
    c = int(input("1) Ingresar otra vez  0) Salir : "))

c = 1
while c > 0:
    age = int(input("¿Cuál es tu edad? "))
    income = float(input("¿Cuales son tus ingresos mensuales?"))
    if age <= 16 or income < 1000:
        print("No tienes que cotizar")
    else:
        print("Tienes que cotizar")
    c = int(input("1) Ingresar otra vez  0) Salir : "))


c = 1
while c <= 1:
    a = input("Escribe tu sexo H / M  : ")
    b = input("Ingrese su nombre :")
    if a.lower() == "M":
        if b.lower() < "m" :
            print("Se encuentra en el Grupo A")
        else:
            print("Se encuntra en el Grupo B")
    else:
        if b.lower() > "n":
            print("Se encuntra en el Grupo A")
        else:
            print("Se encuentra en el Grupo B")
    c = int(input("1) Ingresar otra vez  0) Salir : "))
c = 1
while c > 0:
    p = input("Ingrese su nombre con apeidos : ")
    o = p.split(" ")
    q = " "
    for i in o:
        q += i[0]
    print(q)
    c = int(input("1) Ingresar otra vez  0) Salir : "))

c = 1
while c > 0:
    a = int(input("Ingrese la cantidad de la renta anual : "))
    if a <= 10000:
        print("El inpositivo es del 5%")
    elif 10000 < a <= 20000:
        print("El inpositivo es del 15%")
    elif 20000 < a <= 35000:
        print("El inpositivo es del 20%")
    elif 35000 < a <= 60000:
        print("El inpositivo es del 30%")
    elif a > 60000:
        print("El inpositivo es del 45%")
    c = int(input("1) Ingresar otra vez  0) Salir : "))
'''
c = 1
while c > 0:
    print("La puntación es del 1-100")
    b = float(input("Ingrese la puntación : "))
    a = b/100
    if a < 0.4:
        print("Puntacion : INACEPTABLE");
        print("Cantidad que recibira: ", a * 2400)
    elif 0.4 <= a < 0.6:
        print("Puntacion : ACEPTABLE");
        print("Cantidad que recibira: ", a * 2400)
    elif a >= 0.6:
        print("Puntacion : MERITORIO");
        print("Cantidad que recibira: ", a * 2400)
    c = int(input("1) Ingresar otra vez  0) Salir : "))
        






