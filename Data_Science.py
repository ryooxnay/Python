'''
## Ejemplo 1
x = 10
y = 3
print("10 dividido entre 3 es: ", x/y)
print("El resto de la divicion es: ", x%y)


## Ejemplo 2
x = 100
x > 80 and y <= 95
x > 35 or x < 60
x > 80 and x <= 95
x> 80 and x <= 95 
#fuera [45]: Falso
x> 35 or x <60 
#fuera [46]: verdadero

## Ejemplo 3
x = 100
y = 10
x += y
print("Ejemplo 3: ",x)

##Ejemplo 3.1

x = 15
x += (x * 2)+ 5    
print(x)

## Ejemplo 4 Listas
x = [1,2,3,4,5]
y = ['A','O','G','M']
z = ['A',4,5.1,'M']
print(x[4])
print(x[-5]) #Indica que se busque de derecha a izquierda
print(x[:4]) #Indica que se imprima desde la primera posicion asta el número 4
print(x[2:]) #Indica que se imprima desde la posicion dos asta la ultima.

#Una tupla no se puede cambiar una vez construida, mientras que la lista se puede modificar.
#Una tupla se crea colocando valores separados por comas entre paréntesis () . Considerando que, la lista se crea entre corchetes []
## Elemplo 5 Tuplas

## Ciclo For
k = (1,2,3,4,5)
Estado = ('Delhi','Maharashtra','Karnataka')
for i in k:
    print(i);

#Ejemplo 5.1
for num in range(1,100):
    print(num);

#Ejemplo 5.2
frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
for nombre, color in frutas.items():
    print(nombre, "es de color", color)

#Ciclo While
#permite ejecutar un bloque de instrucciones mientras se cumpla la condición dada.
numero = 0
while numero <= 10:
    print(numero)
    numero +=1;

nombre = " "
while  nombre:
    nombre = input('Escriba un nombre: ') ;

otra = 0
while otra < 1:
    print("")
    print(" BIENVENIDOS A SUCURSALES HUEYTAMALCO ")
    print("1 ) azucar")
    print("2 ) maiz")
    print("3 ) aceite")
    letra = int(input("Ingrese el número del producto a comprar :   "))
    if letra == 1:
        print("$ 30   *Azucar")
    if letra == 2:
        print("$ 10  *Maiz ")
    if letra == 3:
        print("$ 25   *Aceite")
    
    otra = int(input("Decea comprar algo mas 0)SI  1)NO  : "))

## Escriba un numero negativo
num = int(input("Ingrese un numero negativo :  "))
while num >= 0:
    num=int(input("El numero es mayor!! Ingrese uno negativo :  "))
    #num = int(input("Ingrese un numero negativo :  "))  
print("Bien echo & Gracias por su colaboracion...")

        
    
    


## Ejemplo 6 Cuerdas
#Comillas en cadena
palabra = r'Hola "Python"'
print(palabra)
print(palabra[0])
print(palabra[-1])
#Inprimir primera palabra
palabra2 = 'Hola amigo'
pala = palabra2.split()
print(pala[0])

##Ejemplo 7 
##  de listas
#Syntax : list[start : stop : step]
x = [142,124,234,345,465]
y = ['A','C','E','M']
z = ['AA',44,5.1,'KK']
print(x[:3])
print(x[0:3])
print(x[::-1])

#Ejemplo 8 
# sorted(list) -> Ordena de forma ascendente
# sorted(list, reverse = True) -> Ordena de forma decendente
print(sorted(x))
print(sorted(x, reverse = True))

##Ejemplo 9
#Aumentar 5 pociciones 
x = [1, 2, 3, 4, 5]
for i in range(len(x)):
    x[i] = x[i] + 5
print(x)

##Funciones
#Una Función comienza con la palabra clave def seguida del nombre de la función y ()
#El cuerpo de la función comienza con dos puntos (:) 
#La palabra clave return finaliza una función ydar valor a la expresión anterior.
def suma_fun(a,b):
    resul = a + b
    return resul
y = suma_fun(45,10)
def sum_fun2(a,b,c = 100):
    resul2 = a + b + c
    return resul2
z = sum_fun2(45,10)
print(y, " & " , z)


##Declaraciones de condicionales
#Son declaraciones IF ELSE. 
#Nota: Las declaraciones if y else terminan con dos puntos :
o = 0
while o < 1:
    k = int(input("Ingrese el valor para comprobar si es multiplo de 2:  "))
    if k % 2 == 0:
        print("El valor si es multiplo de 2. ")
    else:
        print("El valor no es multiplo de 2.")
    o = int(input("Desea comparar otro número: 0 -> Salir   1 -> Continuar  :: "  ))
#pandas . Para manipulación de datos y disputa de datos. Una colección de funciones para comprender y explorar datos. Es la contraparte de los paquetes dplyr y reshape2 en R
#NumPy . Para computación numérica. Es un paquete para cálculos de matrices eficientes. Nos permite realizar algunas operaciones en una columna o tabla completa en una línea. Es más o menos aproximado al paquete Rcpp en R, que elimina la limitación de velocidad lenta en R.
#Scipy. Para funciones matemáticas y científicas como integración, interpolación, procesamiento de señales, álgebra lineal, estadística, etc. Está construido sobre Numpy.
#Scikit-learn. Una colección de algoritmos de aprendizaje automático. Está construido sobre Numpy y Scipy. Puede realizar todas las técnicas que se pueden hacer en R usando paquetes glm, knn, randomForest, rpart, e1071 .
#Matplotlib. Para visualización de datos. Es un paquete líder para gráficos en Python. Es equivalente al paquete ggplot2 en R.
#Statsmodels. Para modelado estadístico y predictivo. Incluye varias funciones para explorar datos y generar analíticas descriptivas y predictivas. Permite a los usuarios ejecutar estadísticas descriptivas, métodos para imputar valores perdidos, pruebas estadísticas y llevar la salida de la tabla al formato HTML.
#pandasql. Permite a los usuarios de SQL escribir consultas SQL en Python. Es muy útil para las personas que adoran escribir consultas SQL para manipular datos. Es equivalente al paquete sqldf en R.

import pandas as pd
import numpy as np
s1 = pd.Series(np.random.randn(5))
print(s1)
print(s1[1])
print(s1[1:])
'''
##Ejemplo del uso de pandas
#import pandas as pd
#import numpy as np
#mydata = {'código de producto': ['AA', 'AA', 'AA', 'BB', 'BB', 'BB'], 
#'ventas' : [1010, 1025.2, 1404.2, 1251.7, 1160, 1604.8], 
#'cost' : [1020, 1625.2, 1204, 1003.7, 1020, 1124]} 
#df = pd.DataFrame (mydata)
#print(df)

##Como impmortar archivos CSV
#mydata = pd.read_csv("C:\\Users\\USER\Documents\\ISC\\data\\Ch1_bike_sharing_data.csv")
#print(mydata)
## NOTA:Asegúrese de utilizar doble barra invertida al especificar la ruta del archivo CSV.
## Para ver el numero de filas y columas
#print(mydata.shape)

## Para ver las primeras 3 filas
#print(mydata.head(3))
##Para mantener una sola variable, puede escribir en cualquiera de los siguientes tres métodos:
#df.productcode   #df["productcode"]  #df.loc[:,"productcode"]

##Para seleccionar variable por posición de columna, puede usar la función df.iloc . En el siguiente ejemplo, estamos seleccionando la segunda columna. El índice de columna comienza desde 0. Por lo tanto, 1 se refiere a la segunda columna.
#df.iloc[:,1]

##Podemos mantener múltiples variables especificando las variables deseadas dentro de []. Además, podemos hacer uso de la función df.loc ().
#df[["productcode","cost"]]
#df.loc[:,["productcode","cost"]]

#Drop Variable : Podemos eliminar variables usando la función df.drop (). Vea el ejemplo a continuación:
#df2 = df.drop (['ventas'], eje = 1)

#Para resumir el marco de datos
#df.describe ()

#Para resumir todas las variables de carácter , puede utilizar el siguiente script.
#df.describe (incluir = ['O'])
## NOTA: De manera similar, puede usar df.describe (include = ['float64']) para ver el resumen de todas las variables numéricas con decimales.

#Para calcular estadisticas resumidas :: Podemos encontrar manualmente estadísticas resumidas como recuento, media, mediana mediante los siguientes comandos
#df.sales.mean () #df.sales.median () #df.sales.count () #df.sales.min () #df.sales.max ()

#Filtrar datos:: Suponga que se le pide que aplique la condición: el código de producto es igual a "AA" y las ventas son mayores o iguales a 1250.
#df1 = df [(df.productcode == "AA") & (df.sales> = 1250)]

#Ordenar datos :: En el código siguiente, organizamos los datos en orden ascendente por ventas.
#df.sort_values ​​(['ventas'])

#agrupar por: resumen por variable de agrupacion
#df.groupby (df.productcode) .mean ()
#En lugar de resumir para varias variables, puede ejecutarlo para una sola variable, es decir, ventas. Envíe el siguiente script.
#df ["ventas"]. groupby (df.productcode) .mean ()

#Definir variable categórica  df0 = pd.DataFrame ({'id': [1, 1, 2, 3, 1, 2, 2]})
#Definamos como variable categórica. Podemos usar la función astype () para hacer id como una variable categórica.
#df0.id = df0 ["id"]. astype ('categoría')

#Distrubucion de frecuencias
#df ['código de producto']. value_counts ()

#Generar istogramas
#df ['ventas']. hist ()

#BoxPlot
#df.boxplot (columna = 'ventas')

####################################################
#####   CIENCIA DE DATOS CON PYTHON: EJEMPLOS   ###########

#Instalar las bibliotecas nesesarias
import pandas as pd
import statsmodels.api as sm
import numpy as np

## Descargar archivos de la web

df = pd.read_csv("https://stats.idre.ucla.edu/stat/data/binary,csv")
#print(df.shape)
