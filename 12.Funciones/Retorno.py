def entero():
    print('Este es un dato entero:')
    return 10

def decimal():
    print('Este es un dato decimal:')
    return 10

def frase():
    return "Mi nombre es Walter coto"

def asignacion():
    print('Este es un dato entero:')
    return 1,2,3,4,5

print(entero())
print(decimal())
print(frase())

a,b,c,d,e= asignacion()

print(a)
print(b)
print(c)
print(d)
print(e)