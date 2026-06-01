# Promedio de 3 Notas y Estado

# Ingresar las 3 notas
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# Calcular promedio
promedio = (nota1 + nota2 + nota3) / 3

# Determinar estado
if promedio >= 11:
    estado = "Aprobado"
else:
    estado = "Desaprobado"

# Mostrar resultados
print("\nResultados:")
print("Promedio:", promedio)
print("Estado:", estado)