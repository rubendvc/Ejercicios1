num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"
multiplicacion = num1 * num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"División: {division}")
print(f"Multiplicación: {multiplicacion}")
