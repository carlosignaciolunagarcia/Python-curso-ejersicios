from math import sqrt

a=float(input("ingrese el valor de a:"))
b=float(input("ingrese el valor de b:"))
c=float(input("ingrese el valor de c:"))

if ((b**2)-(4*a*c)<0 or a==0):
    print("no se puede calcular")
else:
    #forma1:
    resultado1=(-b+pow((pow(b,2)-(4*a*c)),1/2)) /(2*a)
    resultado2=(-b-pow((pow(b,2)-(4*a*c)),1/2)) /(2*a)

    #forma2
    resultado3=(-b+sqrt(b**2-(4*a*c)))/(2*a)
    resultado4=(-b-sqrt(b**2-(4*a*c)))/(2*a)
    print("R1:",resultado1)
    print("R2:",resultado2)
    print("R3:",resultado3)
    print("R4:",resultado4)
