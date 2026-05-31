# Conversión de Temperatura

# Solicitar temperatura en grados Celsius
celsius = int(input("Ingrese la temperatura en grados Celsius: "))

# Conversiones
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Mostrar resultados
print("\nResultados:")
print("Celsius:", celsius, "°C")
print("Fahrenheit:", fahrenheit, "°F")
print("Kelvin:", kelvin, "K")