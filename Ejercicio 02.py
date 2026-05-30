#Area y perimetro del circulo

import math

#ENTRADA
radio = float(input("Ingrese el radio del circulo: "))

#PROCESO

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

#SALIDA
print(f"El area del circulo es: {area:.2f}") #Se usa :.2f para mostrar con dos decimales
print(f"El perimetro del circulo es: {perimetro:.2f}")
