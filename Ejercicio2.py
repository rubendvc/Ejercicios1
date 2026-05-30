import math
radio = int(input("Ingrese el radio del círculo: "))

perimetro = 2*math.pi*radio
area = math.pi*radio**2 

print(f"Perímetro del círculo: {perimetro: .2f}")
print(f"Área del círculo: {area: .2f}")  