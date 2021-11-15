#librerias importadas
import turtle
import time
import random


#Retrazo de tiempo
posponer = 0.1

#marcador
score = 0
h_score = 0

#Configurar la ventana
wn = turtle.Screen() # Con esto se mostrara otra ventana
wn.title("Juego de la Vivora") #Para cambier el titulo de la ventana
wn.bgcolor("black")     #Para cambiar el color de la ventana
wn.setup(width = 600, height = 600) #Para cambiar el tamaño de la ventana
wn.tracer(0)            #Animaciones mas placenteras para el usuario

#Codigo para crear la cabeza de la serpiente
cbz = turtle.Turtle()   #Para crear un objeto
cbz.speed(0)            #para que al iniciar el juego ya aparezca
cbz.shape("square")     #Para selecionar la figura o forma del objeto
cbz.color("white")      #Para ponerel color de el objeto
cbz.penup()             #Para que no deje un rastro el objeto
cbz.goto(0,0)           #Para que inicie en el centro la cabeza de la vivora
cbz.direction = "stop"  #Para que se espere el objeto a tener una direccion

#Para la comida randon
cm= turtle.Turtle()  #Para crear un objeto
cm.speed(0)         #para que al iniciar el juego ya aparezca
cm.shape("circle")  #Para selecionar la figura o forma del objeto
cm.color("red")     #Para ponerel color de el objeto
cm.penup()          #Para que no deje un rastro el objeto
cm.goto(0,100)        #Para que inicie en el centro la cabeza de la vivora
cm.direction = "stop" #Para que se espere el objeto a tener una direccion

#Cuerpo serpientes
seg = []

#Texto
txt = turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()
txt.goto(0,260)
txt.write("Score : 0    High Score: 0", align = "center", font = ("courier",24, "normal") )

#Funciones
def arriba():
    cbz.direction = "arriba"
def abajo():
    cbz.direction = "abajo"
def derecha():
    cbz.direction = "derecha"
def izquierda():
    cbz.direction = "izquierda"

    
def mov():
    if cbz.direction == "arriba":
        y = cbz.ycor()
        cbz.sety(y + 20)
    if cbz.direction == "abajo":
        y = cbz.ycor()
        cbz.sety(y - 20)
    if cbz.direction == "derecha":
        x = cbz.xcor()
        cbz.setx(x + 20)
    if cbz.direction == "izquierda":
        x = cbz.xcor()
        cbz.setx(x - 20)
#Teclado
wn.listen()  #Funcion que este atenta a los eventos del teclado
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(derecha, "Right")
wn.onkeypress(izquierda, "Left")

#Ciclo de movimiento
while True:
    wn.update()
    #coliciones bordes
    if cbz.xcor() > 280 or cbz.xcor() < -280 or cbz.ycor() > 280 or cbz.ycor() < -280:
        time.sleep(1)
        cbz.goto(0,0)
        cbz.direction = "stop"

        #Esconder los segmentos
        for segme in seg:
            segme.goto(1000,1000)

        #Limpiar segmentos de la lista
        seg.clear()
        #REsetear marcador
        score = 0
        txt.clear()    
        txt.write("Score : {}    High Score: {}".format(score, h_score), align = "center", font = ("courier",24, "normal"))

        
    
    
    #Colicion
    if cbz.distance(cm) < 20:
        x = random.randint(-280, 280)   #para poner la comida
        y = random.randint(-280, 280)
        cm.goto(x,y)                #Para actualizar la comida
        
        ns = turtle.Turtle()   #Para crear un objeto
        ns.speed(0)            #para que al iniciar el juego ya aparezca
        ns.shape("square")     #Para selecionar la figura o forma del objeto
        ns.color("grey")      #Para ponerel color de el objeto
        ns.penup()             #Para que no deje un rastro el objeto
        seg.append(ns)

        #Aumerntar marcador
        score += 10
        if score > h_score:
            h_score = score
        txt.clear()    
        txt.write("Score : {}    High Score: {}".format(score, h_score), align = "center", font = ("courier",24, "normal"))

    #Mover la cola de la serpiente
    totalSeg = len(seg)
    for i in range(totalSeg -1, 0, -1):
        x = seg[i -1].xcor()
        y = seg[i -1].ycor()
        seg[i].goto(x,y)
        
    if totalSeg > 0:
        x = cbz.xcor()
        y = cbz.ycor()
        seg[0].goto(x,y)
    
        
    mov()
    
    #coliciones con el cuerpo
    for segme in seg:
        if segme.distance(cbz) < 20:
            time.sleep(1)
            cbz.goto(0,0)
            cbz.direction = "stop"
             #Esconder los segmentod
            for segme in seg:
                segme.goto(1000,1000)
            seg.clear()

            score = 0
            txt.clear()    
            txt.write("Score : {}    High Score: {}".format(score, h_score), align = "center", font = ("courier",24, "normal"))

                
    time.sleep(posponer)
