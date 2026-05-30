num1 = int(input("Ingrese el numero a evaluar: "))

if num1 % 2 == 0:
    print(f"El número {num1} es par.")
else:
    print(f"El número {num1} es impar.")

if num1 > 0:
    print(f"El número {num1} es positivo.")
elif num1 < 0:
    print(f"El número {num1} es negativo.")
else:
    print(f"El número {num1} es cero.")