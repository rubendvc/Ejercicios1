# Calculadora de IMC con Diagnóstico

# Solicitar datos al usuario
peso = float(input("Ingrese su peso en kg: "))
talla = float(input("Ingrese su talla en metros: "))

# Calcular IMC
imc = peso / (talla ** 2)

# Diagnóstico según OMS
if imc < 18.5:
    diagnostico = "Bajo peso"
elif imc < 25:
    diagnostico = "Normal"
elif imc < 30:
    diagnostico = "Sobrepeso"
elif imc < 35:
    diagnostico = "Obesidad I"
elif imc < 40:
    diagnostico = "Obesidad II"
else:
    diagnostico = "Obesidad III"

# Mostrar resultados
print("\nResultados:")
print("IMC:", round(imc, 2))
print("Diagnóstico:", diagnostico)
