# Calculadora Simple

# Solicitar dos números al usuario  al iniciar 
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Operaciones básicas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Validar división entre cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# Mostrar resultados
print("\nResultados:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)


