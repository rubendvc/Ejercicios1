# Clasificar un Número

# Solicitar número real
numero = float(input("Ingrese un número: "))

# Clasificación: positivo, negativo o cero
if numero > 0:
    tipo = "positivo"
elif numero < 0:
    tipo = "negativo"
else:
    tipo = "cero"

# Verificar si es entero o decimal
if numero.is_integer():
    forma = "entero"
else:
    forma = "decimal"

# Mostrar resultados
print("\nResultados:")
print("El número es", tipo)
print("El número es", forma)