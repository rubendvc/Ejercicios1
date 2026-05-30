# Conversor de Divisas

# Tasas de cambio (puedes ajustarlas)
USD_PEN = 3.80
EUR_PEN = 4.10

# Mostrar menú
print("=== CONVERSOR DE DIVISAS ===")
print("1. Soles a Dólares")
print("2. Dólares a Soles")
print("3. Soles a Euros")
print("4. Euros a Soles")

# Elegir opción
opcion = int(input("Seleccione una opción (1-4): "))

# Ingresar monto
monto = float(input("Ingrese el monto: "))

# Procesar conversión
if opcion == 1:
    resultado = monto / USD_PEN
    print("Equivale a:", round(resultado, 2), "USD")

elif opcion == 2:
    resultado = monto * USD_PEN
    print("Equivale a:", round(resultado, 2), "PEN")

elif opcion == 3:
    resultado = monto / EUR_PEN
    print("Equivale a:", round(resultado, 2), "EUR")

elif opcion == 4:
    resultado = monto * EUR_PEN
    print("Equivale a:", round(resultado, 2), "PEN")

else:
    print("Opción inválida")