import turtle

#Ventana = window = wn
wn = turtle.Screen()
wn.title("P-Pong")
wn.bgcolor("#71EAF7")
wn.setup(width= 800, height= 600)
wn.tracer(0)

#Marcador Variable
marcadorA = 0
marcadorB = 0

#Jugador A
jugadorA= turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("black")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5 , stretch_len= 1)

#Jugador B
jugadorB= turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("black")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5 , stretch_len= 1)

#Pelota
#Jugador A
pelota= turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("blue")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.25
pelota.dy = 0.25

#Linea divisoria
midline = turtle.Turtle()
midline.color("white")
midline.goto(0,400)
midline.goto(0,-400)

#Marcador letras
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador A : 0       Jugador B : 0", align= "center", font=("Courier", 24,))

#pen_final = turtle.Turtle()
#pen_final.speed(0)
#pen_final.color("red")
#pen_final.penup()
#pen_final.hideturtle()
#pen_final.goto(0,0)
#pen_final.write("Juego terminado!")


#Funciones
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

#Teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")





while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    #Bordes der/izq

    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("Jugador A : {}       Jugador B : {}".format(marcadorA,marcadorB), align= "center", font=("Courier", 24,))
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("Jugador A : {}       Jugador B : {}".format(marcadorA,marcadorB), align= "center", font=("Courier", 24,))

    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < jugadorB.ycor() + 50
            and pelota.ycor() > jugadorB.ycor() - 50)):
        pelota.dx *= -1
    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugadorA.ycor() + 50
            and pelota.ycor() > jugadorA.ycor() - 50)):
        pelota.dx *= -1

    if marcadorA == 5 or marcadorB == 5:
        pelota.dx = 0
        pelota.dy = 0