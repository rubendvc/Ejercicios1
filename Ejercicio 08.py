#CALCULADORA DE IMC CON DIAGNOSTICO

#Entrada
peso = float(input("Ingrese su peso en kg: "))
talla = float(input("Ingrese su estatura en m: "))

#Proceso
imc = peso / (talla ** 2)

#salida
print(f"Su IMC es {imc:.2f}")

if imc < 18.5:
    print("Tu categoria es: Bajo peso")
elif imc >= 18.5 and imc < 25:
    print("Tu categoria es: Peso normal")
elif imc >= 25 and imc < 30:
    print("Tu categoria es: Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Tu categoria es: Obesidad tipo I")
elif imc >= 35 and imc < 40:
    print("Tu categoria es: Obesidad tipo II")
else:
    print("Tu categoria es: Obesidad tipo III")