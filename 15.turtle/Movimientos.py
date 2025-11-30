import turtle

s = turtle.Screen() #creamos una instncia de la pantalla (ventana)
t=turtle.Turtle() #se crea un puntero (tortuga)

t.goto(100,100)
t.goto(-100,100)
#t.goto(0,0)
t.home()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

turtle.done()