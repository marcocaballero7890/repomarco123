#Funciones matemáticas
import math 

dato = input("Ingrese un número: ")
dato = int(dato) #convertia entero lo ingresado, reasignación
decibelios = 10 * math.log10(dato) #Función logaritmo de base 10
print(decibelios)