'''
Crear un programa que pida al usuario una letra, 
y si es vocal, muestre el mensaje "Es vocal". 
Sino, decirle al usuario que no es vocal
'''
letra=input("Ingrese una letra: ")

# my codigo
'''
if letra.lower()=="a" or letra.lower()=="e" or letra.lower()=="i" or letra.lower()=="o" or letra.lower()=="u":
    print("La letra es vocal")
else:
    print("La letra no es vocal")
'''

#simplificado
if letra.lower() in "aeiou":
    print("La letra es vocal")
else:
    print("La letra no es vocal")