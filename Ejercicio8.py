peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / altura**2
if imc < 18.5:
    print(f"Su IMC es {imc: .2f} bajo peso.")
elif imc <= 24.9:
    print(f"Su IMC es {imc: .2f} peso normal.")
elif imc <= 29.9:
    print(f"Su IMC es {imc: .2f} sobrepeso.")
elif imc <= 34.9:
    print(f"Su IMC es {imc: .2f} obesidad grado 1.")
elif imc <= 39.9:
    print(f"Su IMC es {imc: .2f} obesidad grado 2.")
else:
    print(f"Su IMC es {imc: .2f} obesidad grado 3.")