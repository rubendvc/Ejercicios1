import math
# Área y Perímetro del Círculo
# Solicitar el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Cálculos
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

# Mostrar resultados
print("\nResultados:")
print("Área del círculo:", area)
print("Perímetro del círculo:", perimetro)
