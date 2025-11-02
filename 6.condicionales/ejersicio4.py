'''
Crear un programa que permita al usuario elegir un candidato 
por el cual votar. Las posibilidades son: 
candidato A por el partido rojo, 
candidato B por el partido verde, 
candidato C por el partido azul. 

Según el candidato elegido (A, B ó C) 
se le debe imprimir el mensaje 
“Usted ha votado por el partido [color que corresponda al candidato
elegido]”. Si el usuario ingresa una opción que no corresponde 
a ninguno de los candidatos disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula
'''

print("Usted puede votar por \ncandidato A por el partido rojo,\ncandidato B por el partido verde.\ncandidato C por el partido azul.")
opcion = input("Ingrese su candidato(A|B|C): ")

if opcion.lower() == "a":
    print("Usted ha votado por el partido rojo")
elif opcion.lower() == "b":
    print("Usted ha votado por el partido verde")
elif opcion.lower() == "c":
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")