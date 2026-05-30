import math
#Ecuación Cuadrática ax² + bx + c = 0:
# Solicitar coeficientes
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Validar que no sea lineal
if a == 0:
    print("No es una ecuación cuadrática.")
else:
    # Calcular discriminante
    discriminante = b**2 - 4*a*c

    # Evaluar casos
    if discriminante > 0:
        # Dos raíces reales
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("\nDos raíces reales:")
        print("x1 =", x1)
        print("x2 =", x2)

    elif discriminante == 0:
        # Raíz doble
        x = -b / (2*a)
        print("\nUna raíz real doble:")
        print("x =", x)

    else:
        # Raíces complejas
        real = -b / (2*a)
        imaginario = math.sqrt(-discriminante) / (2*a)
        print("\nRaíces complejas:")
        print("x1 =", real, "+", imaginario, "i")
        print("x2 =", real, "-", imaginario, "i")