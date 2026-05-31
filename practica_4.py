# Par o Impar

# Solicitar un número entero
numero = int(input("Ingrese un número entero: "))

# Determinar si es par o impar
if numero % 2 == 0:
    tipo = "par"
else:
    tipo = "impar"

# Determinar si es positivo, negativo o cero
if numero > 0:
    signo = "positivo"
elif numero < 0:
    signo = "negativo"
else:
    signo = "cero"

# Mostrar resultados
print("\nResultados:")
print("El número es", tipo)
print("El número es", signo)
