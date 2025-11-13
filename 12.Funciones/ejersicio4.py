'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
y devolver el total de la factura. Si se invoca la función sin pasarle el 
porcentaje de IVA, deberá aplicar un 21%.
'''

def IVA(monto,iva=21):
    return monto * (iva/100) + monto

while True:
    monto=float(input("Ingrese el monto antes de IVA:"))
    iva=float(input("Ingrese el prcentaje de IVA:"))
    
    if monto>=0 and iva>0:
        break
    elif monto>=0 and iva==0:
        iva=21
        break
    else:
        print("no puede existir monto negativo o iva negativo vuelva intentar...\n\n")

resultado=IVA(monto,iva)
print("monto final con iva del %{} incluido es de:{}".format(iva,resultado))