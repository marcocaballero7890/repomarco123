#Funciones matemáticas
import math
grados = 45  #asignamos un valor literal entero a la variable
radianes = grados / 360.0 * 2 * math.pi  #math.pi = constante pi: 3.14...
rad = math.sin(radianes)
print(f"El seno de {grados}° en rad es: {rad:.2f}")  # imprimimos caracteres con las variables, agregamos a la variable rad que se imprimima 2 decimales

print(f"{grados:.2f}° en radianes es: {radianes:15.2f}")
print(f"{grados}° en radianes es: {math.radians(grados):10.2f}")