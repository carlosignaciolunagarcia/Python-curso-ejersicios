#declaracion de variables
num1=40
num2=99.99

#convercion de tipos de numeros float() y int()
print(type(float(num1)))

print(type(int(num2)))

'''operadores
aritmeticas 
con literales'''

print(2+2) #suma
print(150-75)#resta
print(10*10)#multi
print(75/9)#divicion //8.333

print(2**3)#potencia 2*2*2
print(75//9)#division entera //8

print(100%75)#modulo

'''Operaciones 
aritmeticas
con variables'''

num3=10
num4=5
print("-----------------------------------------")
print(num3+num4) #suma
print(num3-num4)#resta
print(num3*num4)#multi
print(num3/num4)#divicion

print(num3**num4)#potencia
print(num3//num4)#division entera

print(num3%num4)#modulo

suma=num3+num4
resta=num3-num4

print("suma=",suma)
print("resta=",resta)

''' 
jerarquia de operaciones
'''
#declaracion de variables
num1=100
num2=50
num3=25
num4=10

print((num1+num2)*(num3-num4)/(num1-num4))