# PROMEDIO DE 3 NOTAS Y ESTADO

#ENTRADA

n1 = float(input("Ingrese la primera nota: "))

if n1 < 0 or n1 > 20:
    print("Nota invalida")

n2 = float(input("Ingrese la segunda nota: "))
if n2 < 0 or n2 > 20:
    print("Nota invalida")

n3 = float(input("ingrese la tercera nota: "))
if n3 < 0 or n3 > 20:
    print("Nota invalida")


#OPERACION

prom = (n1 + n2 + n3) / 3

#SALIDA

if prom < 0 or prom > 20:
    print("Vuelva a ingresar los datos")
else:

    print(f"Tu promedio es {prom:.1f}")

    if prom >= 11:
        print("Estas aprobado")
    else:
        print("estas desaprobado")
