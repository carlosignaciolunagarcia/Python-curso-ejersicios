import turtle

s = turtle.Screen() #creamos una instncia de la pantalla (ventana)
t = turtle.Turtle() #se crea un puntero (tortuga)

#figuras predeterminadas
t.speed(10)  #velocidad de como se pinta la figura, la velocidad va del 1 al 10
t.circle(10)
t.speed(10)
t.circle(50)
t.dot(30)

t.hideturtle()
t.speed(1)
t.circle(40)
t.showturtle()
t.circle(100)

t.setx(100)


turtle.done()