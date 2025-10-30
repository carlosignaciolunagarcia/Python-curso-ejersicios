a=float(input("ingrese el valor de a:"))
b=float(input("ingrese el valor de b:"))
c=float(input("ingrese el valor de c:"))

resultado1=-b+pow((pow(b,2)-(4*a*c)),1/2) /(2*a)
resultado2=-b-pow((pow(b,2)-(4*a*c)),1/2) /(2*a)

print("R1:",resultado1)
print("R2:",resultado2)