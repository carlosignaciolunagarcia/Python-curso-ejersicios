p1=float(input("ingrese la calificacion de la practica1:"))
p2=float(input("ingrese la calificacion de la practica2:"))
p3=float(input("ingrese la calificacion de la practica3:"))
ep=float(input("ingrese la calificacion del examen parcial:"))
ef=float(input("ingrese la calificacion del examen final:"))

pp=(p1+p2+p3)/3
prom=(pp+(2*ep)+(3*ef))/6

print("promedio del alumno es:",prom)