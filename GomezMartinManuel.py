import math

# EJERCICIO 01
# #Calcula el área de un rectángulo	

base = float(input ("Diga la base del rectángulo:"))
altura =float( input ("Diga la altura del rectángulo:"))

def area_rectangulo(base, altura):
    return base * altura

print ("El área del rectángulo es",area_rectangulo(base, altura))

#EJERCICIO 02
#Calcula el área de un círculo

radio = float(input ("Diga el radio del círculo:"))

def area_circulo(radio):
    return math.pi * math.pow(radio,2)

print ("El área del círculo es",area_circulo(radio))


#EJERCICIO 03
#COMPARAR NÚMEROS

a = int(input("Introduce un número para comparar: "))
b= int(input("Introduce otro número para comparar: "))

def relaciona(a,b):
    if a > b :
        return 1
    elif a < b: 
        return -1
    else:
        return 0
    
print(relaciona(a,b))

#EJERCICIO 04
#Intermedio de dos números

a = int(input("Introduce un número para calcular el intermedio: "))
b= int(input("Introduce otro número para calcular el intermedio: "))

def intermedio(a,b):
    return (a+b)/2

print ("El número intermedio es: ",intermedio(a,b))

#Ejercicio 05
#Recortar número

numero = int(input("Introduce un número para recortar: "))
minimo = int(input("Introduce un número mínimo: "))
maximo = int(input("Introduce un número máximo: "))

def recortar(numero,minimo,maximo):
    if numero < minimo: 
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero

print(recortar(numero,minimo,maximo))
#Ejercicio 06
#Listas ordenadas

numeros = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15]
pares = []
impares = []

def separar(numeros):
    for i in numeros : 
        if i%2 == 0:
            pares.append(i)
        else:
            impares.append(i)
separar(numeros)
print("Pares: ", pares)
print("Impares: ", impares)
