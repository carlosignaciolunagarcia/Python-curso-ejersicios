'''
Con el siguiente diccionario, debes crear 
un programa que pregunte al usuario por 
un número; el programa debe imprimir 
el jugador al que hace referencia ese número
'''
Jugadores={
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}

numero=int(input("Cual es el numero que busca:"))

if numero in Jugadores :
    print("El jugador es:",Jugadores[numero])
else:
    print("Jugador no encontrado")