'''
a = "Â¡Hola Mundo!"
print(a)

a = input("Introdusca tu nombre :: ")
n = int(input("Introdusca cuantas veces quiere repetir su nombre :: "))
for i in range(n):
    print("Hola",a)
print(("Hola " + a + "\n") * int(n))

a = input("Introdusca tu nombre :: ")
print(a.upper()," NÃºmero de letras:: ", len(a))

q = int(input("Ingrese el primer dato : "))
w = int(input("Ingrese el primer dato : "))
e = int(input("Ingrese el primer dato : "))
r = int(input("Ingrese el primer dato : "))
t = ((q+w)/(e*r))
print(t)
print(pow(t, 2))

a = int(input("Ingrese las horas trabajadas: "))
b = int(input("Ingrese el precio por hora : "))
print("El sueldo ganado es: $ ", a * b)

a = int(input("Ingrese el dato:  "))
n = (a * ( a + 1 ) ) / 2
print(n)

a = (input("Ingrese cuantos kilos pesas: "))
b = float(input("Ingrse su estatura : "))
print(a / (pow(b,2)))

a = int(input("Ingrese el primer numero : "))
b = int(input("Ingrese el segundo numero : "))
print(a, " entre ", b, " da un cociente de ", a / b, " y un reciduo de ", a % b)

a = float(input("Ingrse la cantidad a inveretir : "))
b = float(input("Ingrese los años que usted quiera invertir : "))
c = float(input("Ingrese el interes anual : "))
print("Si invertimos $", a," a ", b, " años con un interes anual del ", c, "%, vamos a recibir $", a * (c/100 + 1) ** b,2  )

a = int(input("Ingrese la cantidad de payasos comprados: "))
b = int(input("Ingrese la cantidad de muñecas vendidas : "))
print("El ultimo pedido contiene ", a," payasos y ", b, " muñecas, llegando a un total de ", (a * 112 + b * 75), " kg. de peso")

a = float(input("ingrese la cantidad de dinero a depositar : "))
b = 1
for i in range(3):
    c = ((a *1.04))
    print("Año ", b , c)
    a = c 
    b = b+1
'''
a = float(input("Ingrese cuantos panes del dia compra : "))
b = float(input("Ingrese cuantos panes de ayer compra : "))
print("Precio total : $",  (a+b) * 3.49 )
print("Tienen un descuento del 60% los panes de ayer : ")
print("Asi que su total es de : $", (a * 3.49) + (b * 3.49 * .4))
