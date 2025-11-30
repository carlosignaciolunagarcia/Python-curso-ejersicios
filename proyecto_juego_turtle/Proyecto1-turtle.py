import turtle
import random


s = turtle.Screen() #creamos una instncia de la pantalla (ventana)
s.title("Primer proyecto")
s.bgcolor("gray")

jugador1=turtle.Turtle()
jugador2=turtle.Turtle()

jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("green","green")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue","blue")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)
#----------------------------jugador1-------------------------
jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-250,225)
#----------------------------jugador2-------------------------
jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250,-170)
#------------------------------se muestran las totugas-----------
jugador1.showturtle()
jugador2.showturtle()

dado=[1,2,3,4,5,6]

for i in range(20):

    if jugador1.pos() >= (200,200):
        print("la tortuga verde ha ganado")
        break
    elif jugador2.pos() >= (200,200):
        print("la tortuga azul ha ganado")
        break
    else:
        turno1 =input("Presione la tecla enter para avanzar la tortuga azul.")
        turno1 =random.choice(dado)
        print("Tu número es:{} ,\n Avanzas: {}".format(turno1,turno1*20))
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 =input("Presione la tecla enter para avanzar la tortuga verde.")
        turno2=random.choice(dado)
        print("Tu número es:{} ,\n Avanzas: {}".format(turno2,turno2*20))
        jugador2.pendown()
        jugador2.forward(20*turno2)
turtle.done()