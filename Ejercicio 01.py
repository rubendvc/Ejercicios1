# CALCULADORA SIMPLE

#ENTRADA
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

#PROCESO
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2


#SALIDA
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multiplicacion}") # Antes de realizar la division, se verifica que el segundo numero no sea cero.

if num2 != 0:
    division = num1 / num2
    print(f"La division es: {division}")
else:
    print("Error!, no se puede dividir por cero")
