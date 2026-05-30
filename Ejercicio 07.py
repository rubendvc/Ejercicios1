#CLASIFICAR NUMEROS

num = float(input("Ingrese un numero: "))

if num < 0:
    print("El numero es negativo")
elif num > 0:
    print("el numero es positivo")
else:
    print("El numero es cero")


if num % 1 == 0:
    print("El numero es entero")
else:
    print("El numero es decimal")

