# CONVERSION DE TEMPERATURA

#ENTRADA

cel = float(input("Ingrese la temperatura en grados celcius: "))

#PROCESO
Fah = (cel * (9 / 5)) + 32
K = cel + 273.15

#SALIDA
print(f"la temperatura en Fahrenheit es: {Fah}")
print(f"La temperatura en Kelvin es: {K:.2f}")