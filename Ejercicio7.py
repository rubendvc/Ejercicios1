numreal = float(input("Ingrese un número: "))
if numreal > 0:
    print("El número es positivo.")
elif numreal < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

if numreal.is_integer():
    print("El número es un entero.")
else:
    print("El número es un decimal.")